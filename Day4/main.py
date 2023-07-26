import os

def convertToDict(s: str) -> tuple:
    s = s.replace("-", ",")
    l = s.split(sep=",")
    a, b = {"lower": int(l[0]), "upper": int(l[1])}, {"lower": int(l[2]), "upper": int(l[3])}
    if (a["lower"] > b["lower"]):
        a,b = b, a
    return a, b

def checkOverlap(a, b) -> int:
    if (a["lower"] == b["lower"]):
        return 2
    elif (a["upper"] < b["lower"]):
        return 0
    elif(a["upper"] >= b["lower"] and a["upper"] < b["upper"]):
        return 1
    else:
        return 2

with open(os.path.dirname(__file__) + "\\input.txt", "r") as file:
    cntTotal = 0
    cntAtAll = 0
    for line in file:
        if (line.endswith("\n")):
            line = line[:len(line) - 1]
        assignment1, assignment2 = convertToDict(line)
        overlap = checkOverlap(assignment1, assignment2)
        if (overlap == 2):
            cntTotal += 1
            cntAtAll += 1
        elif(overlap == 1):
            cntAtAll += 1
print(f"The amount of elf pairs where one does only work the other already does is {cntTotal}.")
print(f"The amount of elf pairs where one does some work the other already does is {cntAtAll}.")