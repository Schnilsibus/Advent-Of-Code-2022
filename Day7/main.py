from Tree import *
from FileSys import *

import os

def getDirNode(node: Node | Root, dir: str) -> Node:
    childs = node.getChilds()
    for child in childs:
        data = child.getData()
        if (isinstance(data, Dir) and data.getName() == dir):
            return child

def reproduceCommand(root: Root, node: Node | Root, command: list) -> Node | Root:
    if (command[0] == "ls"):
        return node
    elif (command[0] == "cd"):
        if (command[1] == ".."):
            return node._parent
        elif(command[1] == "/"):
            return root
        else:
            return getDirNode(node=node, dir=command[1])
    elif (command[0] == "dir"):
        node.addChilds([Node(node, Dir(command[1])),])
        return node
    else:
        node.addChilds([Node(node, File(command[1], int(command[0]))),])
        return node

def constructFileSystem(commands: list) -> Root:
    root = Root(Dir("/"))
    currentNode = root
    for cmd in commands:
        currentNode = reproduceCommand(root = root, node=currentNode, command=cmd)
    return root

def printNode(node: Node | Root, depth: int):
    tabs = "".join(["   "] * depth)
    d = node.getData()
    print(f"{tabs}-> {d.getName()} ({d.getSize()} B)")
    for child in node.getChilds():
        printNode(node=child, depth=depth + 1)

def calcDirSize(node: Node | Root) -> int:
    if (isinstance(node.getData(), File)):
        return node.getData().getSize()
    sum = 0
    for child in node.getChilds():
        sum += calcDirSize(node=child)
    node.getData().setSize(sum)
    return sum

def getAllSmallDirs(node: Node | Root, size:int) -> list:
    dirs = []
    d = node.getData()
    if (isinstance(d, Dir) and d.getSize() <= size):
        dirs.append(d)
    for child in node.getChilds():
        d = child.getData()
        if (isinstance(d, Dir)):
            dirs.extend(getAllSmallDirs(child, size=size))
    return dirs

with open(os.path.dirname(__file__) + "\\input.txt", "r") as file:
    input = file.readlines()
input = input[1:]
commands = []
for line in input:
    if (line.endswith("\n")):
        line = line[:-1]
    line = line.replace("$", " ")
    commands.append(line.split())
fileSys = constructFileSystem(commands)
calcDirSize(node=fileSys)
printNode(node=fileSys, depth=0)
dirs = getAllSmallDirs(node=fileSys, size=100000)
print(f"The sum of the sizes of all directories that are smaller than 100000B is {sum([d.getSize() for d in dirs])}.")
totalBytes = 70000000
neededBytes = 30000000
currentlyUsedBytes = fileSys.getData().getSize()
currentlyFreeBytes = totalBytes - currentlyUsedBytes
minimumToDeleteBytes = neededBytes - currentlyFreeBytes
allDirs = getAllSmallDirs(node=fileSys, size=totalBytes)
toSmallDirs = getAllSmallDirs(node=fileSys, size=minimumToDeleteBytes-1)
possibleDirs = [d for d in allDirs if d not in toSmallDirs]
sizes = [d.getSize() for d in possibleDirs]
dirToDelete = possibleDirs[sizes.index(min(sizes))]
print(f"The best directory to delete is the {dirToDelete.getName()} directory with {dirToDelete.getSize()} B.")