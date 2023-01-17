from Monkey import Monkey

import numpy as np
import time

class MonkeyGroup:
    def __init__(self, rawMonkeys: list) -> None:
        self._monkeys = [Monkey(m) for m in rawMonkeys]
        self._activityMap = np.zeros(len(self._monkeys), dtype=np.int32)

    def __iter__(self):
        return iter(self._monkeys)

    def __len__(self) -> int:
        return len(self._monkeys)

    def __repr__(self) -> str:
        str = ""
        for i in range(len(self)):
            str = str + f"{i}: {self.getMonkey(nr=i).__repr__()}\n"
        return str

    def __str__(self) -> str:
        str = ""
        for m in self:
            str = str + m.__str__() + "\n\n"
        return str

    def getMonkey(self, nr: int) -> Monkey:
        return self._monkeys[nr]

    def doRound(self, worryDecrease: bool):
        prod = int(np.prod([m._test["denominator"] for m in self]))
        for i in range(len(self)):
            monkey = self.getMonkey(nr=i)
            while (monkey.getItemCount() > 0):
                throwsTo = monkey.doInspection(worryDecrease=worryDecrease, mod=prod)
                self._monkeys[throwsTo["towards"]].addItem(throwsTo["item"])
                self._activityMap[i] += 1

    def doRounds(self, n: int, worryDecrease: bool):
        for i in range(n):
            self.doRound(worryDecrease=worryDecrease)
    
    def getActivityMap(self) -> dict:
        keys = np.arange(len(self))
        return dict(zip(keys, self._activityMap))