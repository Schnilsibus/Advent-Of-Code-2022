class Item:
    def __init__(self, interestLevel: int) -> None:
        self._interestLevel = interestLevel

    def __repr__(self) -> str:
        return "Item: " + str(self._interestLevel)

    def __str__(self) -> str:
        return f"[{str(self._interestLevel)}]"

    def setInterestLevel(self, interestLevel: int):
        self._interestLevel = interestLevel

    def getInterestLevel(self) -> int:
        return self._interestLevel