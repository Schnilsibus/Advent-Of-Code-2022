class CPU:
    def __init__(self) -> None:
        self._x = 1
        self._cycle = 1
        self._pc = 0
        self.resetCurrentOp()

    def nop(self):
        self._opCode = "nop"
        self._opCycles = 1
        self._opStart = self._cycle
    
    def addX(self, param: int):
        self._opCode = "addx"
        self._params = [param,]
        self._opCycles = 2
        self._opStart = self._cycle

    def resetCurrentOp(self):
        self._opCode = ""
        self._opCycles = 0
        self._opStart = 0
        self._params = []

    def executeCurrentOp(self):
        if (self._opCode == "nop"):
            pass
        elif(self._opCode == "addx"):
            self._x += self._params[0]
        self.resetCurrentOp()
        self._pc += 1

    def doCycle(self):
        self._cycle += 1
        if (self._cycle == self._opStart + self._opCycles):
            self.executeCurrentOp()
    
    def getCycle(self) -> int:
        return self._cycle

    def getX(self) -> int:
        return self._x

    def hasOP(self) -> bool:
        return self._opCode != ""
    
    def getPC(self) -> int:
        return self._pc
