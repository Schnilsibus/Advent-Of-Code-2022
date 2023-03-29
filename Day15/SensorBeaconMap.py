def manhattenDistance(pointA: tuple, pointB: tuple) -> int:
    return abs(pointB[0] - pointA[0]) + abs(pointB[1] - pointA[1])

def sortPosListByX(positions: list) -> list:
    positions.sort(key = lambda x: x[0])
    return positions

def tuningFrequency(beaconPos: tuple) -> int:
    return 4000000 * beaconPos[0] + beaconPos[1]

class SensorBeaconPair:
    def __init__(self, sensorPos: tuple, beaconPos: tuple):
        self._sensorPos = sensorPos
        self._beaconPos = beaconPos

    def getManhattenDist(self) -> int:
        return manhattenDistance(self._sensorPos, self._beaconPos)
    
    def getAllImpossiblePositions(self, lineY: int) -> set:
        dist = self.getManhattenDist()
        if (abs(self._sensorPos[1] - lineY) > dist):
            return []
        elif (lineY == self._sensorPos[1]):
            impossiblePos = [(self._sensorPos[0] - dist, lineY), (self._sensorPos[0] - dist, lineY)]
        elif (lineY == self._sensorPos[1] - dist or lineY == self._sensorPos[1] + dist):
            impossiblePos = [(self._sensorPos[0], lineY)]
        else:
            YOffset = lineY - self._sensorPos[1]
            XOffset = dist - abs(YOffset)
            impossiblePos = [(self._sensorPos[0] - XOffset, lineY), (self._sensorPos[0] + XOffset, lineY)]
        if (len(impossiblePos) == 2):
            for x in range(impossiblePos[0][0] + 1, impossiblePos[1][0]):
                impossiblePos.append((x, lineY))
        if (self._beaconPos in impossiblePos):
            impossiblePos.remove(self._beaconPos)
        return set(impossiblePos)
            
class Map:
    def __init__(self):
        self._pairs = []

    def addPair(self, sensorPos: tuple, beaconPos: tuple):
        self._pairs.append(SensorBeaconPair(sensorPos = sensorPos, beaconPos = beaconPos))

    def getimpossibleBeaconPositionsInLine(self, lineY: int) -> set:
        allImpossiblePos = []
        for pair in self._pairs:
            sensorImpossiblePos = pair.getAllImpossiblePositions(lineY = lineY)
            for pos in sensorImpossiblePos:
                if (pos[1] == lineY):
                    allImpossiblePos.append(pos)
        return set(allImpossiblePos)