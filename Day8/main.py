import os

def constructGrid(input: list) -> list:
    grid = []
    for line in input:
        if (line.endswith("\n")):
            line = line[:-1]
        chars = list(line)
        grid.append([int(c) for c in chars])
    return grid

def constructVisibilityMap(grid: list) -> list:
    n, m = len(grid), len(grid[0])
    visibilityMap = []
    for i in range(n):
        row = []
        for i in range(m):
            row.append(False)
        visibilityMap.append(row)
    return visibilityMap

def markVisiblityInLine(gridLine:list, mapLine:list):
    currentMax = -1
    for i in range(len(gridLine)):
        if (gridLine[i] > currentMax):
            mapLine[i] = True
            currentMax = gridLine[i]
        if (currentMax == 9):
            break


def markVisiblity(grid: list, visibilityMap:list):
    n, m = len(grid), len(grid[0])
    for i in range(n):
        lineGrid = list(grid[i])
        lineMap = list(visibilityMap[i])
        markVisiblityInLine(gridLine=lineGrid, mapLine=lineMap)
        visibilityMap[i] = lineMap
        lineGrid.reverse()
        lineMap.reverse()
        markVisiblityInLine(gridLine=lineGrid, mapLine=lineMap)
        lineMap.reverse()
        visibilityMap[i] = lineMap
    for i in range(m):
        lineGrid = [grid[k][i] for k in range(n)]
        lineMap = [visibilityMap[k][i] for k in range(n)]
        markVisiblityInLine(gridLine=lineGrid, mapLine=lineMap)
        for k in range(n):
            visibilityMap[k][i] = lineMap[k]
        lineGrid.reverse()
        lineMap.reverse()
        markVisiblityInLine(gridLine=lineGrid, mapLine=lineMap)
        lineMap.reverse()
        for k in range(n):
            visibilityMap[k][i] = lineMap[k]
        
def countVisibleTrees(visibilityMap: list) -> int:
    cnt = 0
    n, m = len(visibilityMap), len(visibilityMap[0])
    for i in range(n):
        for j in range(m):
            if (visibilityMap[i][j]):
                cnt += 1
    return cnt

def printGrid(grid: list):
    n, m = len(grid), len(grid[0])
    for i in range(n):
        line = "".join([str(t) for t in grid[i]])
        print(line)

def printVisibilityMap(visibilityMap: list):
    n, m = len(visibilityMap), len(visibilityMap[0])
    for i in range(n):
        line = ""
        for j in range(m):
            if (visibilityMap[i][j]):
                line = line + "1"
            else:
                line = line + "0"
        print(line)

def calculateVisibilityAlongLine(line: list, pos:int, height: int) -> tuple:
    res = []
    n = len(line)
    cnt = 0
    while (pos + cnt - 1 >= 0):
        cnt -= 1
        if (line[pos + cnt] >= height):
            break
    res.append(-1 * cnt)
    cnt = 0
    while (pos + cnt + 1 < n):
        cnt += 1
        if (line[pos + cnt] >= height):
            break
    res.append(cnt)
    return tuple(res)

def claculateTreeScore(x: int, y: int, grid: list) -> int:
    n, m = len(grid), len(grid[0])
    row = list(grid[x])
    col = [grid[k][y] for k in range(n)]
    treeHeight = grid[x][y]
    up,down = calculateVisibilityAlongLine(line=col, pos=x, height=treeHeight)
    left, right = calculateVisibilityAlongLine(line=row, pos=y, height=treeHeight)
    return up * down * left * right

def findTreeWithHighesScore(grid: list) -> tuple:
    n, m = len(grid), len(grid[0])
    currentMax = 0
    currentPos = (0,0)
    for i in range(n):
        for j in range(m):
            score = claculateTreeScore(x=i, y=j, grid=grid)
            if (score > currentMax):
                currentMax=score
                currentPos = (i, j)
    return currentPos


with open(os.path.dirname(__file__) + "\\PuzzleInput.txt", "r") as file:
    input = file.readlines()

grid = constructGrid(input=input)
visibilityMap = constructVisibilityMap(grid=grid)
markVisiblity(grid=grid, visibilityMap=visibilityMap)
visibleTrees = countVisibleTrees(visibilityMap=visibilityMap)
print(f"There are {visibleTrees} trees visible.")
bestTree = findTreeWithHighesScore(grid=grid)
scenicScore = claculateTreeScore(bestTree[0], bestTree[1], grid)
print(f"The tree with the highest scenic score is the tree at {bestTree} with score {scenicScore}.")