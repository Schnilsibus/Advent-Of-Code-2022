class File:
    def __init__(self, name: str, size: int) -> None:
        self._name = name
        self._size = size

    def getName(self) -> str:
        return self._name
    
    def getSize(self) -> int:
        return self._size

    def setName(self, name: str):
        self._name = name

    def setSize(self, size: int):
        self._size = size

class Dir:
    def __init__(self, name: str, size: int = -1) -> None:
        self._name = name
        self._size = size

    def getName(self) -> str:
        return self._name
    
    def getSize(self) -> int:
        return self._size

    def setName(self, name: str):
        self._name = name

    def setSize(self, size: int):
        self._size = size