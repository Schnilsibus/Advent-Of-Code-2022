import os

def getMaxOfDict(d: dict, n: int) -> list:
    d_copy = dict(d)
    k = list(d.keys())
    v = list(d.values())
    if (n == 0):
        return list()
    else:
        keys = [k[v.index(max(v))], ]
        d_copy.pop(keys[0])
        keys.extend(getMaxOfDict(d_copy, n - 1))
        return keys

currentElfIndex = 1
currentElfCalories = 0
elfs = {}
with open(os.path.dirname(__file__) + "\\input.txt", "r") as file:
    for line in file:
        if (line.endswith("\n")):
            line = line[:len(line) - 1]
        if (line != ""):
            currentElfCalories += int(line)
        else:
            elfs.update({currentElfIndex : currentElfCalories})
            currentElfIndex += 1
            currentElfCalories = 0
max_keys = getMaxOfDict(elfs, 3)
print("The top three elfs are:")
for key in max_keys:
    print(f"Elf Nr. {key} with {elfs.get(key)} calories.")
print(f"The elf with the most calories has {elfs.get(max_keys[0])} calories.")
print(f"The top three elfs together have {sum(elfs[k] for k in max_keys)} calories.")




