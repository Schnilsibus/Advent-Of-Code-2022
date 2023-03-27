def manhattenDistance(pointA: tuple, pointB: tuple) -> int:
    return abs(pointB[0] - pointA[0]) + abs(pointB[1] - pointA[1])

class SensorBeaconPair:
    def __init__(self, sensorPos: tuple, beaconPos: tuple):
        self._sensorPos = sensorPos
        self._beaconPos = beaconPos

    def getManhattenDist(self) -> int:
        return manhattenDistance(self._sensorPos, self._beaconPos)
    
    def getAllImpossiblePositions(self) -> tuple:
        dist = self.getManhattenDist()
        impossiblePos = []
        for xOffset in range(dist):
            yOffset = dist - xOffset
            impossiblePos.append((self._sensorPos[0] + xOffset, self._sensorPos[1] + yOffset))
            impossiblePos.append((self._sensorPos[0] + xOffset, self._sensorPos[1] - yOffset))
            impossiblePos.append((self._sensorPos[0] - xOffset, self._sensorPos[1] + yOffset))
            impossiblePos.append((self._sensorPos[0] - xOffset, self._sensorPos[1] - yOffset))
        return tuple(impossiblePos)
            

class Map:
    def __init__(self):
        self._pairs = []

    def addPair(self, sensorPos: tuple, beaconPos: tuple):
        self._pairs.append(SensorBeaconPair(sensorPos = sensorPos, beaconPos = beaconPos))

    def getimpossibleBeaconPositionsInLine(self, lineY: int) -> tuple:
        allImpossiblePos = []
        for pair in self._pairs:
            sensorImpossiblePos = pair.getAllImpossiblePositions()
            print(len(sensorImpossiblePos))
            for pos in sensorImpossiblePos:
                if (pos[1] == lineY):
                    allImpossiblePos.append(pos)
        return tuple(allImpossiblePos)