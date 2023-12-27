import sys
import numpy as np
import operator
import os

testFileName = str(sys.argv[1])
trainingFileName = str(sys.argv[2])

def createDataSet(dirname):
    labels = []
    trainingFileList = [entry.name for entry in os.scandir(dirname) if entry.is_file()]
    m = len(trainingFileList)
    matrix = np.zeros((m, 1024))

    for i in range(m):
        fileNameStr = trainingFileList[i]
        answer = int(fileNameStr.split('_')[0])
        labels.append(answer)
        matrix[i, :] = getVector(os.path.join(dirname, fileNameStr))
    return matrix, labels 

def classify0(inX, dataSet, labels, k): 
    dataSetSize = dataSet.shape[0]
    diffMat = np.tile(inX, (dataSetSize, 1)) - dataSet
    sqDiffMat = diffMat ** 2 
    sqDistances = sqDiffMat.sum(axis=1) 
    distances = sqDistances ** 0.5 
    sortedDistIndicies = distances.argsort() 
    classCount = {} 

    for i in range(k): 
        voteIlabel = labels[sortedDistIndicies[i]] 
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    
    return sortedClassCount[0][0]

def getVector(filename):
    vector = np.zeros((1, 1024))
    with open(filename) as f:
        for i in range(32):
            line = f.readline()
            for j in range(32):
                vector[0, 32 * i + j] = int(line[j])
    return vector        

# main
trainingFile = sys.argv[1]
testFile = sys.argv[2]

fileList = [entry.name for entry in os.scandir(testFile) if entry.is_file()]
length = len(fileList)

matrix, labels = createDataSet(trainingFile)

for k in range(1, 20, 2):
    data, error = 0, 0
    
    for i in range(length):
        answer = int(fileList[i].split('_')[0])
        testData = getVector(os.path.join(testFile, fileList[i]))
        result = classify0(testData, matrix, labels, k)
        
        data += 1
        if answer != result :
            error += 1
    
    print(int(error / data * 100))
