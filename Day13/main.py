def readInupt(path: str) -> list:
    def removeNewLines(input: list) -> list:
        for i in range(len(input)):
            if (input[i].endswith("\n")):
                input[i] = input[i][:-1]
        return input
    import os
    with open(os.path.dirname(__file__) + path, "r") as file:
        input = removeNewLines(input = file.readlines())
    return input

def converInput(input: list) -> list:
    result = []
    import json
    from Packet import Packet
    for i in range((len(input) + 1) // 3):
        leftRaw = json.loads(input[3 * i])
        rightRaw = json.loads(input[(3 * i) + 1])
        result.append({"left": Packet(rawData = leftRaw), "right": Packet(rawData = rightRaw), "comp": None})
    return result

def solvePart1() -> str:
    input = readInupt(path = "\\PuzzleInput.txt")
    pairs = converInput(input=input)
    for pair in pairs:
        pair["comp"] = pair["left"] < pair["right"]
    indexSum = sum([i + 1 for i in range(len(pairs)) if pairs[i]["comp"] == 1])
    return f"The sum off the indexes of pairs that are out of order is {indexSum}"

def solvePart2():
    pass

print(solvePart1())
print(solvePart2())
