import numpy as np

class HeightMap:
    def __init__(self, rawMap: list):
        def createMapFromRawMap(rawMap: list) -> np.ndarray:
            map = np.ndarray(shape = (self._height, self._width), dtype = np.uint16)
            for y in range(self._height):
                for x in range(self._width):
                    map[y][x] = rawMap[y][x]
            return map
        
        self._height, self._width = len(rawMap), len(rawMap[0])
        self._map = createMapFromRawMap(rawMap = rawMap)

    def __repr__(self) -> str:
        return f"Map: {(self._height, self._width)}"

    def __str__(self) -> str:
        return self._map.__str__()

    def getPossibleSteps(self, pos: tuple) -> dict:
        y, x = pos
        possibleSteps = {"up": False, "down": False, "left": False, "right": False, }
        maxAccessibleHeight = self._map[y][x] + 1
        if (y - 1 >= 0 and self._map[y - 1][x] <= maxAccessibleHeight):
            possibleSteps["up"] = True
        if (y + 1 < self._height and self._map[y + 1][x] <= maxAccessibleHeight):
            possibleSteps["down"] = True
        if (x - 1 >= 0 and self._map[y][x - 1] <= maxAccessibleHeight):
            possibleSteps["left"] = True
        if (x + 1 < self._width and self._map[y][x + 1] <= maxAccessibleHeight):
            possibleSteps["right"] = True
        return possibleSteps

    def getPossibleInvertedSteps(self, pos: tuple) -> dict:
        y, x = pos
        possibleSteps = {"up": False, "down": False, "left": False, "right": False, }
        minAccessibleHeight = self._map[y][x] - 1
        if (y - 1 >= 0 and self._map[y - 1][x] >= minAccessibleHeight):
            possibleSteps["up"] = True
        if (y + 1 < self._height and self._map[y + 1][x] >= minAccessibleHeight):
            possibleSteps["down"] = True
        if (x - 1 >= 0 and self._map[y][x - 1] >= minAccessibleHeight):
            possibleSteps["left"] = True
        if (x + 1 < self._width and self._map[y][x + 1] >= minAccessibleHeight):
            possibleSteps["right"] = True
        return possibleSteps

    def getShape(self) -> tuple:
        return (self._height, self._width)

    def getHeightOfPos(self, pos: tuple) -> int:
        y, x = pos
        return self._map[y][x]