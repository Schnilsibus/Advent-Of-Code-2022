class CaveStoneScan:
    def __init__(self):
        self._stonePoints = {}
        self.floorLevel = 0

    def __eq__(self, other):
        if (isinstance(other, self.__class__)):
            return self._stonePoints == other._stonePoints
        else:
            return False
    
    def addStonePoint(self, pos: tuple):
        self._stonePoints[pos] = None
        if (pos[1] + 2 > self.floorLevel):
            self.floorLevel = pos[1] + 2

    def addStonePoints(self, positions: list):
        for pos in positions:
            self.addStonePoint(pos = pos)

    def addLine(self, startPos: tuple, endPos: tuple):
        def constuctVerticalLine() -> list:
            line = []
            if (startPos[1] < endPos[1]):
                for yCoord in range(startPos[1], endPos[1] + 1):
                    line.append((startPos[0], yCoord))
            else:
                for yCoord in range(endPos[1], startPos[1] + 1):
                    line.append((startPos[0], yCoord))
            return line
        def constuctHorizontalLine() -> list:
            line = []
            if (startPos[0] < endPos[0]):
                for xCoord in range(startPos[0], endPos[0] + 1):
                    line.append((xCoord, startPos[1]))
            else:
                for xCoord in range(endPos[0], startPos[0] + 1):
                    line.append((xCoord, startPos[1]))
            return line
        if (startPos[0] == endPos[0]):
            line = constuctVerticalLine()
        else:
            line = constuctHorizontalLine()
        self.addStonePoints(positions = line)

    def addPath(self, points: list):
        for i in range(1, len(points)):
            self.addLine(startPos = points[i -1], endPos = points[i])

    def isStone(self, pos: tuple):
        return pos[1] == self.floorLevel or pos in self._stonePoints.keys()
    
    def getFloorY(self):
        return self.floorLevel

    def getLowestY(self):
        allYs = [p[1] for p in list(self._stonePoints.keys())]
        return max(allYs)
    
    def getMostLeftX(self):
         allXs = [p[0] for p in list(self._stonePoints.keys())]
         return min(allXs)

    def getMostRightX(self):
        allXs = [p[0] for p in list(self._stonePoints.keys())]
        return max(allXs)

class CaveSandScan:
    def __init__(self):
        self._sandPoints = {}

    def __eq__(self, other):
        if (isinstance(other, self.__class__)):
            return self._sandPoints == other._sandPoints
        else:
            return False
    
    def addSandPoint(self, pos: tuple):
        self._sandPoints[pos] = None
    
    def isSand(self, pos: tuple):
        return pos in self._sandPoints.keys()

    def getGrainCount(self) -> int:
        return len(self._sandPoints)

class Simulation:
    def __init__(self, stoneScan: CaveStoneScan, spawn: tuple, ignoreFloor: bool):
        self._stoneScan = stoneScan
        self._sandScan = CaveSandScan()
        self._previousSimulatedGrainPosition = tuple()
        self._latestSimulatedGrainPosition = tuple()
        self._spawn = spawn
        self._abyss = self._stoneScan.getLowestY() + 1
        self._ignoreFloor = ignoreFloor
        self.spawnSimulatedGrain()

    def spawnSimulatedGrain(self):
        self._latestSimulatedGrainPosition = self._spawn

    def cementSimulatedGrain(self):
        self._sandScan.addSandPoint(self._latestSimulatedGrainPosition)

    def isBlocked(self, pos: tuple) -> bool:
        return self._stoneScan.isStone(pos = pos) or self._sandScan.isSand(pos = pos)

    def hasSimulatedGrainMoved(self):
        return not self._latestSimulatedGrainPosition == self._previousSimulatedGrainPosition

    def hasSimulatedGrainFallenToAbyss(self):
        return self._latestSimulatedGrainPosition[1] >= self._abyss
    
    def isSpawnCemented(self):
        return self._sandScan.isSand(pos = self._spawn)
    
    def hasSimulationFinished(self):
        if (self._ignoreFloor):
            return self.hasSimulatedGrainFallenToAbyss()
        else:
            return self.isSpawnCemented()

    def swapGrainPositions(self):
        self._latestSimulatedGrainPosition, self._previousSimulatedGrainPosition = self._previousSimulatedGrainPosition, self._latestSimulatedGrainPosition

    def moveSimulatedGrain(self):
        x, y = self._latestSimulatedGrainPosition[0], self._latestSimulatedGrainPosition[1]
        if (not self.isBlocked(pos = (x, y + 1))):
            self._previousSimulatedGrainPosition = (x, y + 1)
        elif (not self.isBlocked(pos = (x - 1, y + 1))):
            self._previousSimulatedGrainPosition = (x - 1, y + 1)
        elif (not self.isBlocked(pos = (x + 1, y + 1))):
            self._previousSimulatedGrainPosition = (x + 1, y + 1)
        else:
            self._previousSimulatedGrainPosition = self._latestSimulatedGrainPosition
        self.swapGrainPositions()

    def sectionToString(self, upperLeft: tuple, lowerRight: tuple) -> str:
        strBuilder = ""
        for i in range(upperLeft[1], lowerRight[1] + 1, 1):
            for j in range(upperLeft[0], lowerRight[0] + 1 , 1):
                if (self._spawn == (j, i)):
                    strBuilder += "+"
                elif (self._latestSimulatedGrainPosition == (j, i)):
                    strBuilder += "o"
                elif(self._sandScan.isSand(pos = (j, i))):
                    strBuilder += "0"
                elif(self._stoneScan.isStone(pos = (j, i))):
                    strBuilder += "#"
                else:
                    strBuilder += "."
            strBuilder += "\n"
        return strBuilder
    
    def simulateStep(self) -> bool:
        self.moveSimulatedGrain()
        if (not self.hasSimulatedGrainMoved()):
            self.cementSimulatedGrain()
            self.spawnSimulatedGrain()
            return False
        return True

    def simulateGrain(self):
        while (self.simulateStep() and not (self._ignoreFloor and self.hasSimulatedGrainFallenToAbyss())):
            pass

    def animate(self, singleStep: bool, upperLeft: tuple, lowerRight: tuple, fps: int, n: int = 0):
        from os import system
        from time import sleep
        execute = self.simulateStep if singleStep else self.simulateGrain
        if (n == 0):
            while (not self.hasSimulationFinished()):
                execute()
                sleep(1.0/fps)
                system("cls")
                print(self.sectionToString(upperLeft = upperLeft, lowerRight = lowerRight))
        else:
            for i in range(n):
                if (self.isSpawnCemented()):
                    break
                execute()
                sleep(1.0/fps)
                system("cls")
                print(self.sectionToString(upperLeft = upperLeft, lowerRight = lowerRight))

    def simulate(self, singleStep: bool, n: int = 0):
        execute = self.simulateStep if singleStep else self.simulateGrain
        if (n == 0):
            while (not self.hasSimulationFinished()):
                execute()
        else:
            for i in range(n):
                execute()

    def getCementedGrainsCount(self):
        return self._sandScan.getGrainCount()
        