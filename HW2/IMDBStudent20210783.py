#!/usr/bin/python3
fileName = input()

genreList = []
genreDict = {}
total = []

try:
    with open(fileName, "rt") as f:
        line = f.readlines()
        line = [str.rstrip('\n') for str in line]

        for i in line:
            lines = i.split("::")

            for i in range(0, len(lines), 2):
                if i != 0:
                    genreList.append(lines[i])

        for j in range(0, len(genreList)):
            genreSplit = genreList[j].split("|")

            for k in genreSplit:
                if '\\n' in k:
                    genre = k.split('\\')[0]
                else:
                    genre = k

                if genre not in genreDict:
                    genreDict.setdefault(k, 0)
                    genreDict[genre] += 1
                else:
                    genreDict[genre] += 1

        print(genreDict)

        outputName = fileName.replace(fileName, "movieoutput.txt")

    with open(outputName, "w") as output:
        for i in genreDict.keys():
            output.write(i+" "+str(genreDict[i])+"\n")

except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")
