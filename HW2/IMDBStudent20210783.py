import sys

fileName = str(sys.argv[1])

genreList = []
genreDict = {}

try:
    with open(fileName, "rt", encoding='UTF-8') as f:
        line = f.readlines()
        line = [str.rstrip('\n') for str in line]

        for i in line:
            lines = i.split("::")

            for i in range(0, len(lines), 2):
                if i != 0:
                    genreList.append(lines[i])

        for j in range(0, len(genreList)):
            genreSplit = genreList[j].split("|")

            for genre in genreSplit:
                if genre not in genreDict:
                    genreDict.setdefault(genre, 0)
                    genreDict[genre] += 1
                else:
                    genreDict[genre] += 1

        outputName = sys.argv[2]

    with open(outputName, "w") as output:
        for i in genreDict.keys():
            output.write(i+" "+str(genreDict[i])+"\n")

except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")
