from HeightMap import HeightMap
from Graph import Graph
from PosNode import PosNode
import os

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

def convertHeightMapToGraph(map: HeightMap) -> Graph:
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
    return graph
        

with open(os.path.dirname(__file__) + "\\PuzzleInput.txt", "r") as file:
    input = removeNewLines(input = file.readlines())
startEndDict = findStartAndEnd(input = input)
map = convertInputToHeightMap(input=input)
graph = convertHeightMapToGraph(map = map)