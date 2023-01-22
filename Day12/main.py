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

def minDistanceToHeight(g: Graph, map: HeightMap, start: int, height: int, path: list = []) -> int:
    prefix = "".join(["| "]*len(path))
    if (map.getHeightOfPos(pos = g[start].getPos()) == height):
        print(f"{prefix}{start} -> {0}")
        return 0
    print(f"{prefix}{start}")
    adjacentNodes = g.getAdjacentNodes(index = start)
    nextSteps = [n for n in adjacentNodes if n not in path]
    path.append(start)
    distances = [minDistanceToHeight(g=g, map=map, start=n, height=height, path=path) for n in nextSteps]
    path.remove(start)
    if (len(distances) == 0):
        print(f"{prefix}{start} -> {len(g) + 1}")
        return len(g) + 1
    else:
        print(f"{prefix}{start} -> {min(distances) + 1}")
        return min(distances) + 1


with open(os.path.dirname(__file__) + "\\MyInput.txt", "r") as file:
    input = removeNewLines(input = file.readlines())
startPos = findStartAndEnd(input = input)["start"]
endPos = findStartAndEnd(input = input)["end"]
map = convertInputToHeightMap(input=input)
graph = convertHeightMapToGraph(map = map)["graph"]
posIndexMap = convertHeightMapToGraph(map = map)["posIndexMap"]
distancesFromStart = dijkstra(g = graph, start = posIndexMap[startPos])
print(f"The fewest number of steps to get to the location with the best signal is {distancesFromStart[posIndexMap[endPos]]}")
print(minDistanceToHeight(g=graph, map=map, start=posIndexMap[endPos], height=1))