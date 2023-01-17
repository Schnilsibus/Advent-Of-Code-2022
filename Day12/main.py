from HeightMap import HeightMap
from Graph import Graph
from PosNode import PosNode
import os
import time

def removeNewLines(input: list) -> list:
    for i in range(len(input)):
        if (input[i].endswith("\n")):
            input[i] = input[i][:-1]
    return input

def findStartAndEnd(input: list) -> dict:
    y, x = len(input), len(input[0])
    for i in range(0, y):
        for j in range(0, x):
            char = input[i][j]
            if (char == "S"):
                start = (i, j)
            elif(char == "E"):
                end = (i, j)
    return {"start": start, "end": end}

def convertInputToHeightMap(input: list) -> HeightMap:
    y, x = len(input), len(input[0])
    raw = []
    for i in range(0, y):
        raw.append([])
        for j in range(0, x):
            char = input[i][j]
            if (char == "S"):
                start = (j, i)
                char = "a"
            elif (char == "E"):
                end = (j, i)
                char = "z"
            raw[i].append( ord(char) - 96)
    map = HeightMap(rawMap=raw)
    return map

def convertHeightMapToGraph(map: HeightMap) -> dict:
    y, x = map.getShape()
    graph = Graph()
    posIndexMap = {}
    for i in range(0, y):
        for j in range(0, x):
            index = graph.addNode(node = PosNode(pos = (i, j)))
            posIndexMap[(i, j)] = index
    for node in graph:
        pos = node.getPos()
        posibleSteps = map.getPossibleSteps(pos = pos)
        if (posibleSteps["up"]):
            graph.addAdjacentNode(tailIndex = node.getIndex(), headIndex = posIndexMap[(pos[0] - 1, pos[1])], bidirectional = False)
        if (posibleSteps["down"]):
            graph.addAdjacentNode(tailIndex = node.getIndex(), headIndex = posIndexMap[(pos[0] + 1, pos[1])], bidirectional = False)
        if (posibleSteps["left"]):
            graph.addAdjacentNode(tailIndex = node.getIndex(), headIndex = posIndexMap[(pos[0], pos[1] - 1)], bidirectional = False)
        if (posibleSteps["right"]):
            graph.addAdjacentNode(tailIndex = node.getIndex(), headIndex = posIndexMap[(pos[0], pos[1] + 1)], bidirectional = False)
    return {"graph": graph, "posIndexMap": posIndexMap}
        
def dijkstra(g: Graph, start: int) -> list:
    infinity = len(g) + 1
    d = [0] * len(g)
    notRelaxed = {n.getIndex():infinity for n in g.getNodes()}
    notRelaxed[start] = 0
    while (len(notRelaxed) > 0):
        index = min(notRelaxed, key = notRelaxed.get)
        d[index] = notRelaxed[index]
        adjacentNodes = g.getAdjacentNodes(index = index)
        for i in adjacentNodes:
            if (i in notRelaxed):
                notRelaxed[i] = notRelaxed[index] + 1
        del notRelaxed[index]
    return d

def floydWarshall(g: Graph) -> dict:
    infinity = len(g) + 1
    d = {(s, e): infinity for s in range(len(g)) for e in range(len(g))}
    for s in range(len(g)):
        d[(s, s)] = 0
        adjacentNodes = g.getAdjacentNodes(index = s)
        for e in adjacentNodes:
            d[(s, e)] = 1
    for w in range(len(g)):
        for u in range(len(g)):
            for v in range(len(g)):
                x = d[(u, w)] + d[(w, v)]
                if (d[(u, v)] > x):
                    d[(u, v)] = x
    return d

def getAllGroundNodes(m: HeightMap) -> list:
    groundLevel = []
    y, x = m.getShape()
    for i in range(y):
        for j in range(x):
            if (m.getHeightOfPos(pos = (i, j)) == 1):
                groundLevel.append((i, j))
    return groundLevel

def calculateLevelDistances(level: list, end: int) -> dict:
    distances = {}
    for n in level:
        tBefore = time.time_ns()
        distances[n] = dijkstra(g = graph, start = n)[end]
        tAfter = time.time_ns()
        print(f"done with {n} in {(tAfter - tBefore) / 1000000:.2f} ms")
    return distances

def specificDijkstraWithAbort(g: Graph, start: int, end: int, maxLength: int) -> int:
    infinity = len(g) + 1
    notRelaxed = {n.getIndex():infinity for n in g.getNodes()}
    notRelaxed[start] = 0
    while (len(notRelaxed) > 0):
        index = min(notRelaxed, key = notRelaxed.get)
        if (index == end):
            return max([notRelaxed[index], maxLength])
        adjacentNodes = g.getAdjacentNodes(index = index)
        for i in adjacentNodes:
            if (i in notRelaxed):
                notRelaxed[i] = notRelaxed[index] + 1
        del notRelaxed[index]

def calculateClosestSquareInLevelWithBranchSkipping(level: list, g: Graph, end: int, maxLength: int) -> dict:
    currentShortesPathLength = maxLength
    for n in level:
        tBefore = time.time_ns()
        d = specificDijkstraWithAbort(g = g, start = n, end = end, maxLength = maxLength)
        if (currentShortesPathLength > d):
            currentShortesPathLength = d
        tAfter = time.time_ns()
        print(f"done with {n} in {(tAfter - tBefore) / 1000000:.2f} ms")
    return currentShortesPathLength

with open(os.path.dirname(__file__) + "\\PuzzleInput.txt", "r") as file:
    input = removeNewLines(input = file.readlines())
startPos = findStartAndEnd(input = input)["start"]
endPos = findStartAndEnd(input = input)["end"]
map = convertInputToHeightMap(input=input)
graph = convertHeightMapToGraph(map = map)["graph"]
posIndexMap = convertHeightMapToGraph(map = map)["posIndexMap"]
distancesFromStart = dijkstra(g = graph, start = posIndexMap[startPos])
print(f"The fewest number of steps to get to the location with the best signal is {distancesFromStart[posIndexMap[endPos]]}")
groundLevel = [posIndexMap[pos] for pos in getAllGroundNodes(m = map)]
minDist = calculateLevelDistances(level = groundLevel, end = posIndexMap[endPos])
print(f"The fewest number of steps to get to the location with the best signal from any square with elevation a is {minDist}")
