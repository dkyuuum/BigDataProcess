# #!/usr/bin/python3
# import sys
from datetime import datetime
import sys

fileName = sys.argv[1]
weekDay = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
vehiclesDict = {}
tripsDict = {}

try:
    with open(fileName, "rt", encoding='UTF-8') as f:
        lines = f.readlines()
        lines = [str.rstrip('\n') for str in lines]

        for line in lines:
            uber = line.split(",")
            region = uber[0]
            date = uber[1]
            vehicles = int(uber[2])
            trips = int(uber[3])

            day = datetime.strptime(date, "%m/%d/%Y").strftime("%a").upper()

            index = f"{region},{day}"
            if index in vehiclesDict:
                vehiclesDict[index] += vehicles
            else:
                vehiclesDict[index] = vehicles

            if index in tripsDict:
                tripsDict[index] += trips
            else:
                tripsDict[index] = trips

        print(vehiclesDict)
        outputName = sys.argv[2]

    with open(outputName, "w") as output:
        tripsValue = tripsDict

        for key, vehiclesValue in vehiclesDict.items():
            output.write(f"{key} {vehiclesValue},{tripsValue[key]}\n")

except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")
