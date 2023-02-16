class CaveScan:
    def __init__(self):
        self._stonePoints = {}
    
    def addStonePoint(self, pos: tuple):
        self._stonePoints[pos] = None

    def addStonePoints(self, positions: list):
        for pos in positions:
            self.addStonePoint(pos = pos)

    def addLine(self, startPos: tuple, endPos: tuple):
        def constuctVerticalLine() -> list:
            line = []
            for yOffset in range(abs(startPos[1] - endPos[1]) + 1):
                line.append((startPos[0], startPos[1] + yOffset))
            return line
        def constuctHorizontalLine() -> list:
            line = []
            for xOffset in range(abs(startPos[0] - endPos[0]) + 1):
                line.append((startPos[0] - xOffset, startPos[1]))
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
        return pos in self._stonePoints.keys()

    def getSection(self, upperLeft: tuple, lowerRight: tuple) -> list:
        n, m = lowerRight[0] - upperLeft[0] + 1, lowerRight[1] - upperLeft[1] + 1
        section = list()
        for i in range(m):
            section.append(list())
            for j in range(n):
                pos = (upperLeft[0] + j, upperLeft[1] + i)
                section[i].append(True if self.isStone(pos = pos) else False)
        return section

    def getSectionAsString(self, upperLeft: tuple, lowerRight: tuple) -> str:
        section = self.getSection(upperLeft = upperLeft, lowerRight = lowerRight)
        for i in range(len(section)):
            line = section[i]
            line = ["#" if pos == True else "." for pos in line]
            section[i] = "".join(line)
        return "\n".join(section)