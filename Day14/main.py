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
    from CaveSystem import CaveStoneScan, Simulation
    input = readInupt(path = "\\PuzzleInput.txt")
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
    caveScan = convertInputToCaveStoneScan(input = input)
    simulation = Simulation(stoneScan = caveScan, spawn = (500, 0))
    upperLeft, lowerRight = (caveScan.getMostLeftX(), 0), (caveScan.getMostRightX(), caveScan.getLowestY())
    simulation.simulate(singleStep = False)
    print(simulation.sectionToString(upperLeft = upperLeft, lowerRight = lowerRight))
    # Animation / simulation looks fine --> error probably in the conversion of input to CaveStoneScan
    return f"{str(simulation.getCementedGrainsCount())} units of sand come to rest before the sand flows into the abyss below"

def solvePart2() -> str:
    return "not solved"


print(solvePart1())
print(solvePart2())
