import sys
from os import listdir
import numpy as np
import operator

trainingFile = sys.argv[1]
testFile = sys.argv[2]
labels = []


def classify(inX, dataSet, labels, k):
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
    sortedClassCount = sorted(classCount.items(),
                              key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]


def setDataSet(dataSetList):
    trainingFileList = listdir(dataSetList)
    matrix = np.zeros((len(trainingFileList), 32*32))

    for i in range(len(trainingFileList)):
        fileName = trainingFileList[i]
        labels.append(int(fileName.split('_')[0]))
        matrix[i, :] = getList(dataSetList + '/' + fileName)
    return matrix, labels


def getList(file):
    vertex = np.zeros((1, 32*32))
    with open(file) as f:
        for j in range(32):
            line = f.readline()

            for k in range(32):
                vertex[0, 32 * j + k] = int(line[k])
        return vertex


testList = listdir(testFile)
matrix, labels = setDataSet(trainingFile)

for k in range(1, 21, 2):
    data = 0
    error = 0

    for i in range(len(testList)):
        answer = int(testList[i].split('_')[0])
        testData = getList(testFile + '/' + testList[i])
        result = classify(testData, matrix, labels, k)

        data += 1
        if answer != result:
            error += 1

    print(int(error / data * 100))
