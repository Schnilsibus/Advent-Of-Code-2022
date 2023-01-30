class Packet:
    def __init__(self, rawData: list):
        self._data = rawData

    def __lt__(self, other):
        return Packet.compare(self.getData(), other.getData())

    def __str__(self) -> str:
        return str(self._data)

    def __repr__(self) -> str:
        return str(self)

    def getData(self) -> list:
        return self._data

    def setData(self, rawData: list):
        self._data = rawData

    @staticmethod
    def compare(left: list | int, right: list | int) -> int:
        if (type(left) == type(right) and type(left) == int):
            if (left == right):
                return 0
            return 1 if left < right else -1
        elif (type(left) == type(right) and type(left) == list):
            zipped = zip(left, right)
            for elem in zipped:
                result = Packet.compare(elem[0], elem[1])
                if (result != 0):
                    return result
            if (len(left) == len(right)):
                return 0
            else:
                return 1 if len(left) < len(right) else -1
        elif (type(left) == int):
            return Packet.compare(left = [left,], right = right)
        elif (type(right) == int):
            return Packet.compare(left = left, right = [right,])
        

