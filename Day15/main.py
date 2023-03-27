from SensorBeaconMap import Map

def readInupt(path: str) -> list:
    def removeNewLines(input: list) -> list:
        for i in range(len(input)):
            if (input[i].endswith("\n")):
                input[i] = input[i][:-1]
        return input
    import os
    with open(os.path.dirname(__file__) + path, "r") as file:
        input = removeNewLines(input = file.readlines())
    return input

def convertInput(input: list):
    separators = ["Sensor at x=",  ", y=", ": closest beacon is at x="]
    map = Map()
    for line in input:
        for separator in separators:
            line = line.replace(separator, ",")
        values = [int(s) for s in line.split(",")[1:]]
        sensorPos = tuple(values[:2])
        beaconPos = tuple(values[2:])
        map.addPair(sensorPos = sensorPos, beaconPos = beaconPos)
    return map

def solvePart1() -> str:
    # idea: for all pairs check if it is even in range; calculate the two out most posisitons on the line; fill in the rest --> do brnach skipping
    lineY = 2000000
    map = convertInput(input = readInupt(path = "\\PuzzleInput.txt"))
    impossiblePos = map.getimpossibleBeaconPositionsInLine(lineY = lineY)
    print(f"\n\n{len(impossiblePos)}\n")
    return "notsolved"

def solvePart2() -> str:
    return "notsolved"

print(solvePart1())
print(solvePart2())
