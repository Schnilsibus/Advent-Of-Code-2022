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

def solvePart1() -> str:
    input = readInupt(path = "\\PuzzleInput.txt")
    def converInputToPairs(input: list) -> list:
        result = []
        import json
        from Packet import Packet
        for i in range((len(input) + 1) // 3):
            leftRaw = json.loads(input[3 * i])
            rightRaw = json.loads(input[(3 * i) + 1])
            result.append({"left": Packet(rawData = leftRaw), "right": Packet(rawData = rightRaw), "comp": None})
        return result
    pairs = converInputToPairs(input=input)
    for pair in pairs:
        pair["comp"] = pair["left"] < pair["right"]
    indexSum = sum([i + 1 for i in range(len(pairs)) if pairs[i]["comp"] == 1])
    return f"The sum off the indexes of pairs that are out of order is {indexSum}"

def solvePart2() -> str:
    from Packet import Packet
    input = readInupt(path = "\\PuzzleInput.txt")
    def convertInputToList(input: list) -> list:
        result = []
        import json
        for line in input:
            if (not line == ""):
                result.append(Packet(rawData= json.loads(line)))
        return result
    packets = convertInputToList(input = input)
    seperators = [Packet(rawData = [[2]]), Packet(rawData = [[6]])]
    packets.extend(seperators)
    import functools
    packets.sort(key = functools.cmp_to_key(Packet.__cmp__))
    return f"The decoder key is {(packets.index(seperators[0]) + 1) * (packets.index(seperators[1]) + 1)}"


print(solvePart1())
print(solvePart2())
