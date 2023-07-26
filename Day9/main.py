import os

def convertInput(input: list) -> list:
    commands = []
    for line in input:
        if (line.endswith("\n")):
            line = line[:-1]
        l = line.split()
        commands.append([l[0], int(l[1])])
    return commands

def moveHead(pos: list, dir: str):
    if (dir == "U"):
        pos[0] = (pos[0][0], pos[0][1] + 1)
    elif (dir == "D"):
        pos[0] = (pos[0][0], pos[0][1] - 1)
    elif (dir == "L"):
        pos[0] = (pos[0][0] + 1, pos[0][1])
    else:
        pos[0] = (pos[0][0] - 1, pos[0][1])

def moveTail(pos: list, knot: int):
    HPos = pos[knot - 1]
    TPos = pos[knot]
    if (abs(HPos[0] - TPos[0]) <= 1 and abs(HPos[1] - TPos[1]) <= 1):
        pass
    elif(HPos[0] == TPos[0]):
        if (HPos[1] > TPos[1]):
            TPos = (TPos[0], TPos[1] + 1)
        else:
            TPos = (TPos[0], TPos[1] - 1)
    elif(HPos[1] == TPos[1]):
        if (HPos[0] > TPos[0]):
            TPos = (TPos[0] + 1, TPos[1])
        else:
            TPos = (TPos[0] - 1, TPos[1])
    else:
        x, y = 0, 0
        if (HPos[0] > TPos[0]):
            x = 1
        else:
            x = -1
        if (HPos[1] > TPos[1]):
            y = 1
        else:
            y = -1
        TPos = (TPos[0] + x, TPos[1] + y)
    pos[knot - 1] = HPos
    pos[knot] = TPos

def doStep(pos: list, dir: str, knots: int) -> tuple:
    moveHead(pos=pos, dir=dir)
    for i in range(1, knots):
        moveTail(pos=pos, knot=i)
    return pos[knots - 1]

def simulateCommand(pos: list, command: list, knots:int) -> list:
    visitedPos = set()
    for i in range(command[1]):
        visitedPos.add(doStep(pos=pos, dir=command[0], knots=knots))
    return visitedPos

def simulateRope(sequence: list, knots: int) -> set:
    pos = []
    for i in range(knots):
        pos.append((0, 0))
    visitedPos = set([pos[knots - 1],])
    for cmd in sequence:
        visitedPos.update(simulateCommand(pos=pos, command=cmd, knots=knots))
    return visitedPos

with open(os.path.dirname(__file__) + "\\input.txt", "r") as file:
    input = file.readlines()

sequence = convertInput(input=input)
visitedPos = simulateRope(sequence=sequence, knots=2)
print(f"The tail of the rope (with 2 knots) visits {len(visitedPos)} different position during the simulation.")
visitedPos = simulateRope(sequence=sequence, knots=10)
print(f"The tail of the rope (with 10 knots) visits {len(visitedPos)} different position during the simulation.")