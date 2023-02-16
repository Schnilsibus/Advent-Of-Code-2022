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


def solvePart1() -> str:
    from CaveSystem import CaveScan
    input = readInupt(path = "\\Example.txt")
    def convertInputToCaveScan(input: list) -> CaveScan:
        paths = []
        for inputLine in input:
            positions = []
            posStrings = inputLine.split(" -> ")
            for posString in posStrings:
                x, y = [int(s) for s in posString.split(",")]
                positions.append((x, y))
            paths.append(positions)
        print(paths)
        scan = CaveScan()
        for path in paths:
            scan.addPath(path)
        print(scan.getSectionAsString(upperLeft = (494, 0), lowerRight = (503, 9)))
    caveScan = convertInputToCaveScan(input = input)
    return "not solved"

def solvePart2() -> str:
    return "not solved"


print(solvePart1())
print(solvePart2())
