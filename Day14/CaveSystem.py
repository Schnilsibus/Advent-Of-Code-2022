class Position(dict):
    def __init__(self, x: int, y: int):
        dict.__init__(self, {"x": x, "y":y})

class CaveScan:
    def __init__(self):
        self._stonePoints = []
    
    def addStonePoint(self, pos: Position):
        self._stonePoints[pos] = None

    def addStonePoints(self, positions: list):
        for pos in positions:
            self.addStonePoint(pos = pos)

    def addLine(self, startPos: Position, endPos: Position):
        def constuctVerticalLine() -> list:
            line = []
            for yOffset in range(abs(startPos["y"]-endPos["y"]) + 1):
                line.append(Position(x = startPos["x"], y = startPos["y"] + yOffset))
        def constuctHorizontalLine() -> list:
            line = []
            for xOffset in range(abs(startPos["x"]-endPos["x"]) + 1):
                line.append(Position(x = startPos["x"] + xOffset, y = startPos["y"]))
        if (startPos["x"] == endPos["x"]):
            line = constuctVerticalLine()
        else:
            line = constuctHorizontalLine()
        self.addStonePoints(positions = line)

    def isStone(self, pos: Position):
        return pos in self._stonePoints.keys()