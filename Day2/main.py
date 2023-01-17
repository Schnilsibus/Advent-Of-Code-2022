import os

oppPlays = {
    "A": 1,
    "B": 2,
    "C": 3
}
myPlays = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

WinOrLose = {
    "X": -1,
    "Y": 0,
    "Z": 1
}

def getOldPlays(s: str) -> tuple:
    l = s.split(sep=" ")
    return (oppPlays.get(l[0]), myPlays.get(l[1]))

def calculateScore(opp: int, me: int) -> int:
    o,m = opp-1, me-1
    if (o == m):
        outcome = 3
    elif ((o + 1) % 3 == m):
        outcome = 6
    else:
        outcome = 0
    return me + outcome
    
def getNewPlays(s: str) -> tuple:
    l = s.split(sep=" ")
    return (oppPlays.get(l[0]), (oppPlays.get(l[0]) - 1 + WinOrLose.get(l[1])) % 3 + 1)

oldScore, newScore = 0,0
with open(os.path.dirname(__file__) + "\\PuzzleInput.txt", "r") as file:
    for line in file:
        if (line.endswith("\n")):
            line = line[:len(line) - 1]
        opp_play, my_play = getOldPlays(s=line)
        oldScore += calculateScore(opp=opp_play, me=my_play)
        opp_play, my_play = getNewPlays(s=line)
        newScore += calculateScore(opp=opp_play, me=my_play)

print(f"The total missinterpreted score is {oldScore}.")
print(f"The total correct score is {newScore}.")