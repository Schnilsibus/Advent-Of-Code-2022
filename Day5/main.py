import os

def convertStacks(inp: list) -> list:
    n = int((len(inp[0]) + 1) / 4)
    stacks = []
    for i in range(0, n):
        stacks.append([])
    for line in inp:
        for i in range(0, n):
            c = line[(i * 4) + 1]
            if (c != " "):
                stacks[i].append(c)
    return stacks

def printStacks(stacks: list):
    for stack in stacks:
        print(stack)

def convertSequence(inp: list) -> list:
    sequence = []
    for line in inp:
        l = line.split()
        sequence.append([int(l[i]) for i in [1, 3, 5]])
    return sequence

def executeStep(stacks, step):
    s = stacks[step[1] - 1]
    d = stacks[step[2] - 1]
    for i in range(0, step[0]):
        d.append(s.pop())

def execute(stacks, seqence):
    for step in sequence:
        executeStep(stacks, step)

def executeStep9001(stacks, step):
    s = stacks[step[1] - 1]
    d = stacks[step[2] - 1]
    d.extend(s[step[0] * -1:])
    stacks[step[1] - 1] = s[:step[0] * -1]

def execute9001(stacks, seqence):
    for step in sequence:
        executeStep9001(stacks, step)

with open(os.path.dirname(__file__) + "\\input.txt", "r") as file:
    lines = file.readlines()
for i in range(0, len(lines)):
    if (lines[i].endswith("\n")):
        lines[i] = lines[i][:len(lines[i]) - 1]
sep = lines.index("")
stacksStr = lines[:sep-1]
stacksStr.reverse()
sequenceStr = lines[sep+1:]
stacks = convertStacks(stacksStr)
sequence = convertSequence(sequenceStr)
execute(stacks, sequence)
tops = [s[-1] for s in stacks]
print(f"The containers on top of each stack after rerearranging are: -{''.join(tops)}-.")
stacks9001 = convertStacks(stacksStr)
sequence9001 = convertSequence(sequenceStr)
execute9001(stacks9001, sequence9001)
tops9001 = [s[-1] for s in stacks9001]
print(f"The containers on top of each stack after rerearranging with 9001 crane are: -{''.join(tops9001)}-.")