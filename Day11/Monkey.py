from Item import Item

class Monkey:
    def __init__(self, rawMonkeyData: dict) -> None:
        self._items = [Item(i) for i in rawMonkeyData["items"]]
        self._operation = dict(rawMonkeyData["op"])
        self._test = dict(rawMonkeyData["test"])

    def __repr__(self) -> str:
        return "Monkey: " + " ".join([str(i) for i in self._items])

    def __str__(self) -> str:
        items = "items: " + " ".join([str(i) for i in self._items]) + "\n"
        op = "operation: " + " ".join([str(i) for i in self._operation.values()]) + "\n"
        d, t, e = self._test["denominator"], self._test["true"], self._test["false"]
        test = "test: " + str(t) + " if div " + str(d) + " else " + str(e)
        return items + op + test
    
    def addItem(self, item: Item):
        self._items.append(item)
    
    def doInspection(self, worryDecrease: bool, mod: int) -> dict:
        item = self._items.pop()
        nr = self.decideForItem(item=item, worryDecrease=worryDecrease)
        self.trimInterestLevel(item=item, mod=mod)
        return {"towards": nr, "item": item}

    def decideForItem(self, item: Item, worryDecrease: bool):
        self.setNewInterestLevel(item, worryDecrease=worryDecrease)
        if (self.performTest(item)):
            return self._test["true"]
        else:
            return self._test["false"]

    def setNewInterestLevel(self, item: Item, worryDecrease: bool):
        level = item.getInterestLevel()
        a, b = None, None
        if (isinstance(self._operation["a"], str)):
            a = level
        elif (isinstance(self._operation["a"], int)):
            a = self._operation["a"]
        if (isinstance(self._operation["b"], str)):
            b = level
        elif (isinstance(self._operation["b"], int)):
            b = self._operation["b"]
        if (self._operation["op"] == "+"):
            item.setInterestLevel(a+b)
        elif (self._operation["op"] == "*"):
            item.setInterestLevel(a*b)
        if (worryDecrease):
            item.setInterestLevel(item.getInterestLevel() // 3)

    def performTest(self, item: Item) -> bool:
        return item.getInterestLevel() % self._test["denominator"] == 0

    def trimInterestLevel(self, item: Item, mod: int):
        level = item.getInterestLevel()
        level %= mod
        item.setInterestLevel(level)

    def getItemCount(self) -> int:
        return len(self._items)