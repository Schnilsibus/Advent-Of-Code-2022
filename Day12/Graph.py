from Node import Node

class Graph:
    def __init__(self):
        self._nodes = []
        self._adjacencySet = []

    def __repr__(self) -> str:
        return f"Graph: n:{len(self._nodes)}"

    def __str__(self) -> str:
        strBuilder = ""
        for i in range(len(self)):
            nodeRep = f"{str(self._nodes[i])} -> ["
            for index in self._adjacencySet[i]:
                nodeRep += f"{str(index)}, "
            if (len(self._adjacencySet[i]) == 0):
                strBuilder += nodeRep + "]\n"
            else:
                strBuilder += nodeRep[:-2] + "]\n"
        return strBuilder

    def __iter__(self):
        return iter(self._nodes)

    def __len__(self):
        return len(self._nodes)

    def getNodes(self) -> list:
        return self._nodes

    def getNode(self, index: int) -> Node:
        return self._nodes[index]

    def getAdjacentNodes(self, index: int) -> list:
        adjacentNodes = self._adjacencySet[index]
        return [self._nodes[i] for i in adjacentNodes]
    
    def addNode(self, node: Node = Node()) -> int:
        node.setIndex(index = len(self))
        self._nodes.append(node)
        self._adjacencySet.append(set())
        return len(self) - 1

    def addAdjacentNode(self, tailIndex: int, headIndex: int, bidirectional: bool = False):
        self._adjacencySet[tailIndex].add(headIndex)
        if (bidirectional):
            self._adjacencySet[headIndex].add(tailIndex)
