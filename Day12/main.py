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
        possibleSteps = map.getPossibleSteps(pos = pos)
        if (possibleSteps["up"]):
            graph.addAdjacentNode(tailIndex = node.getIndex(), headIndex = posIndexMap[(pos[0] - 1, pos[1])], bidirectional = False)
        if (possibleSteps["down"]):
            graph.addAdjacentNode(tailIndex = node.getIndex(), headIndex = posIndexMap[(pos[0] + 1, pos[1])], bidirectional = False)
        if (possibleSteps["left"]):
            graph.addAdjacentNode(tailIndex = node.getIndex(), headIndex = posIndexMap[(pos[0], pos[1] - 1)], bidirectional = False)
        if (possibleSteps["right"]):
            graph.addAdjacentNode(tailIndex = node.getIndex(), headIndex = posIndexMap[(pos[0], pos[1] + 1)], bidirectional = False)
    return {"graph": graph, "posIndexMap": posIndexMap}

def convertHeightMapToInvertedGraph(map: HeightMap, posIndexMap: list, orgGraph: Graph) -> Graph:
    y, x = map.getShape()
    graph = Graph()
    for n in orgGraph:
        graph.addNode(n) # possible error source (maybe iterator changes order then old map n other stuff dont work)
        pos = n.getPos()
        possibleSteps = map.getPossibleInvertedSteps(pos = pos)
        if (possibleSteps["up"]):
            graph.addAdjacentNode(tailIndex = n.getIndex(), headIndex = posIndexMap[(pos[0] - 1, pos[1])], bidirectional = False)
        if (possibleSteps["down"]):
            graph.addAdjacentNode(tailIndex = n.getIndex(), headIndex = posIndexMap[(pos[0] + 1, pos[1])], bidirectional = False)
        if (possibleSteps["left"]):
            graph.addAdjacentNode(tailIndex = n.getIndex(), headIndex = posIndexMap[(pos[0], pos[1] - 1)], bidirectional = False)
        if (possibleSteps["right"]):
            graph.addAdjacentNode(tailIndex = n.getIndex(), headIndex = posIndexMap[(pos[0], pos[1] + 1)], bidirectional = False)
    return graph
        
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

def getLevel(g: Graph, map: HeightMap, posTable: dict, height: int) -> list:
    level = []
    for i in range(len(g)):
        if (map.getHeightOfPos(pos = g[i].getPos()) == height):
            level.append(i)
    return level


with open(os.path.dirname(__file__) + "\\PuzzleInput.txt", "r") as file:
    input = removeNewLines(input = file.readlines())
startPos = findStartAndEnd(input = input)["start"]
endPos = findStartAndEnd(input = input)["end"]
map = convertInputToHeightMap(input=input)
graph = convertHeightMapToGraph(map = map)["graph"]
posIndexMap = convertHeightMapToGraph(map = map)["posIndexMap"]
distancesFromStart = dijkstra(g = graph, start = posIndexMap[startPos])
print(f"The fewest number of steps to get to the location with the best signal is {distancesFromStart[posIndexMap[endPos]]}")
invertedGraph = convertHeightMapToInvertedGraph(map = map, posIndexMap = posIndexMap, orgGraph = graph)
groundLevel = getLevel(g = invertedGraph, map = map, posTable = posIndexMap, height = 1)
distancesFromEnd = dijkstra(g = invertedGraph, start = posIndexMap[endPos])
distancesToGroundLevel = [distancesFromEnd[i] for i in range(len(distancesFromEnd)) if i in groundLevel]
print(f"The fewest number of steps to the locaion with the best signal from any point with elevation a is {min(distancesToGroundLevel)}")