from CaveSystem import CaveStoneScan, Simulation

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

def convertInputToCaveStoneScan(input: list) -> CaveStoneScan:
        paths = []
        for inputLine in input:
            positions = []
            posStrings = inputLine.split(" -> ")
            for posString in posStrings:
                x, y = [int(s) for s in posString.split(",")]
                positions.append((x, y))
            paths.append(positions)
        scan = CaveStoneScan()
        for path in paths:
            scan.addPath(path)
        return scan

def solvePart1() -> str:
    input = readInupt(path = "\\PuzzleInput.txt")
    caveScan = convertInputToCaveStoneScan(input = input)
    simulation = Simulation(stoneScan = caveScan, spawn = (500, 0), ignoreFloor = True)
    simulation.simulate(singleStep = False)
    return f"{str(simulation.getCementedGrainsCount())} units of sand came to rest before the sand flows into the abyss below"

def solvePart2() -> str:
    input = readInupt(path = "\\PuzzleInput.txt")
    caveScan = convertInputToCaveStoneScan(input = input)
    floorY = caveScan.getFloorY()
    leftX = caveScan.getMostLeftX()
    rightX = caveScan.getMostRightX()
    simulation = Simulation(stoneScan = caveScan, spawn = (500, 0), ignoreFloor = False)
    simulation.simulate(singleStep = False)
    return f"{str(simulation.getCementedGrainsCount())} units of sand came to rest before the source of the sand becomes blocked"

print(solvePart1())
print(solvePart2())
