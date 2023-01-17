from Node import Node

class PosNode(Node):
    def __init__(self, pos: tuple):
        Node.__init__(self)
        self._pos = pos

    def getPos(self) -> tuple:
        return self._pos

    def setPos(self, pos: tuple):
        self._pos = pos