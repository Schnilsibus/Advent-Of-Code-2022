class Root:
    def __init__(self, data) -> None:
        self._childs = []
        self._data = data
    
    def addChilds(self, childs: list):
        self._childs.extend(childs)

    def removeChilds(self, childs: list):
        self._childs = [ele for ele in self._childs if ele not in childs]

    def getChilds(self) -> list:
        return self._childs

    def getData(self) -> object:
        return self._data
    
    def setData(self, data):
        self._data = data


class Node:
    def __init__(self, parent, data) -> None:
        self._parent = parent
        self._childs = []
        self._data = data

    def addChilds(self, childs: list):
        self._childs.extend(childs)

    def removeChilds(self, childs: list):
        self._childs = [ele for ele in self._childs if ele not in childs]
    
    def getChilds(self) -> list:
        return self._childs

    def getData(self) -> object:
        return self._data
    
    def setData(self, data):
        self._data = data