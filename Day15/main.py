from SensorBeaconMap import Map

files = {"input": "PuzzleInput", "example": "Example"}
lineYs = {"input": 2000000, "example": 10}

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
    run = "input"
    map = convertInput(input = readInupt(path = f"\\{files[run]}.txt"))
    result = map.getimpossibleBeaconPositionsInLine(lineY = lineYs[run])
    return f"In the line with y={lineYs[run]} are {len(result)} positions that cannot contain a beacon"

def solvePart2() -> str:
    return "notsolved"

print(solvePart1())
print(solvePart2())
