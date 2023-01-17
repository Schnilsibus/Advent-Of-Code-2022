import os

def convertToSortedCompartmentsWithPrio(s: str) -> tuple:
    n = len(s)
    backpack = list()
    for c in s:
        v = ord(c)
        if (v > 90):
            backpack.append(v - 96)
        else:
            backpack.append(v - 38)
    comp1, comp2 = backpack[:int(n/2)], backpack[int(n/2):]
    comp1.sort(); comp2.sort()
    return comp1, comp2

def convertToSortedBackpackWithPrio(s: str) -> list:
    n = len(s)
    backpack = list()
    for c in s:
        v = ord(c)
        if (v > 90):
            backpack.append(v - 96)
        else:
            backpack.append(v - 38)
    backpack.sort()
    return backpack

def findCommonElementOfSortedLists(l1: list, l2:list) -> int:
    it1, it2 = 0, 0
    while (it1 < len(l1) and it2 < len(l2)):
        if (l1[it1] == l2[it2]):
            return l1[it1]
        elif (l1[it1] < l2[it2]):
            it1 += 1
        else:
            it2 += 1
    return None

def allIteratorsInBounds(iter: list, lists: list) -> bool:
    for i in range(0, len(iter)):
        if (iter[i] >= len(lists[i])):
            return False
    return True

def allIteratorsHaveSameElement(iter: list, lists: list) -> bool:
    ele0 = lists[0][iter[0]]
    for i in range(1, len(iter)):
        ele = lists[i][iter[i]]
        if (ele0 != ele):
            return False
    return True

def incrementMinIterator(iter: list, lists: list):
    values = list()
    for i in range(0, len(iter)):
        values.append(lists[i][iter[i]])
    to_inc = values.index(min(values))
    min_iter = iter[to_inc]
    iter[to_inc] = min_iter +1

def findCommonElementsOfSortedLists(t: list) -> list:
    n = len(t)
    commonElements = list()
    iterators = [0] * n
    while (allIteratorsInBounds(iter=iterators, lists=t)):
        if (allIteratorsHaveSameElement(iter=iterators, lists=t)):
            commonElements.append(t[0][iterators[0]])
        incrementMinIterator(iter=iterators, lists=t)
        
        
    return commonElements

with open(os.path.dirname(__file__) + "\\PuzzleInput.txt", "r") as file:
    wrongItems = list()
    for line in file:
        if (line.endswith("\n")):
            line = line[:len(line) - 1]
        compartment1, compartment2 = convertToSortedCompartmentsWithPrio(s=line)
        wrongItems.append(findCommonElementOfSortedLists(compartment1, compartment2))
print(f"The sum of the priorities of all items in both compartments is {sum(wrongItems)}.")

with open(os.path.dirname(__file__) + "\\PuzzleInput.txt", "r") as file:
    cnt = 0
    group = [None] * 3
    allBadges = []
    for line in file:
        if (line.endswith("\n")):
            line = line[:len(line) - 1]
        group[cnt % 3] = convertToSortedBackpackWithPrio(line)
        if (cnt % 3 == 2):
            commons = list(set(findCommonElementsOfSortedLists(group)))
            allBadges.extend(commons)
        cnt += 1
print(f"The sum of the priorities of all badges is {sum(allBadges)}.")
        