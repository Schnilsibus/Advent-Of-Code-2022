class Node:
    def __init__(self):
        self._index = -1

    def __repr__(self) -> str:
        return f"Node: {self._index}"

    def __str__(self) -> str:
        return f"[{self._index}]"

    def getIndex(self) -> int:
        return self._index
    
    def setIndex(self, index: int):
        self._index = index