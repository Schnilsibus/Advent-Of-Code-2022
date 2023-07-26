from MonkeyGroup import MonkeyGroup
import numpy as np

import os

def convertInput(input: list) -> MonkeyGroup:
    monkeys = []
    monkey = {}
    for i in range(len(input)):
        line = str(input[i]).strip()
        if (line.endswith("\n")):
            line = line[:-1]
        type = i % 7
        if (type == 1):
            line = line.replace("Starting items: ", "")
            items = line.split(sep=", ")
            monkey["items"] = [int(k) for k in items]
        elif (type == 2):
            line = line.replace("Operation: new = ", "")
            line = line.replace("old", "x")
            op = line.split()
            vals = [int(e) if e.isdigit() else e for e in op]
            keys = ["a", "op", "b"]
            monkey["op"] = dict(zip(keys, vals))
        elif (type == 3):
            test = {}
            line = line.replace("Test: divisible by ", "")
            test["denominator"] = int(line)
        elif(type == 4):
            line = line.replace("If true: throw to monkey ", "")
            test["true"] = int(line)
        elif(type == 5):
            line = line.replace("If false: throw to monkey ", "")
            test["false"] = int(line)
            monkey["test"] = test
            monkeys.append(monkey)
            monkey = {}
    return MonkeyGroup(monkeys)

with open(os.path.dirname(__file__) + "\\input.txt", "r") as file:
    input = file.readlines()
monkeys = convertInput(input=input)
monkeys.doRounds(n=20, worryDecrease=True)
activityMap = monkeys.getActivityMap()
activityMap = sorted(activityMap.items(), key=lambda x:x[1], reverse=True)
mostActivMonkeys = activityMap[:2]
print(f"The level of monkey buissness after 20 rounds with decreasing levels of worry is {np.prod([m[1] for m in mostActivMonkeys])}.")
monkeys = convertInput(input=input)
monkeys.doRounds(n=10000, worryDecrease=False)
activityMap = monkeys.getActivityMap()
activityMap = sorted(activityMap.items(), key=lambda x:x[1], reverse=True)
mostActivMonkeys = [int(activityMap[0][1]), int(activityMap[1][1])]
print(f"The level of monkey buissness after 10000 rounds without decreasing levels of worry is {mostActivMonkeys[0] * mostActivMonkeys[1]}.")