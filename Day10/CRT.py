import numpy as np

class CRT:
    def __init__(self) -> None:
        self._cycle = 1
        self._screenHeight = 6
        self._screenWidth = 40
        self._screen = np.zeros((self._screenHeight, self._screenWidth))

    def doCycle(self, x: int):
        pixel = self._cycle % 241
        yPos = (pixel - 1) // self._screenWidth
        xPos = (pixel - yPos * self._screenWidth) - 1
        self.drawPixel(x=x, pos=(xPos, yPos))
        self._cycle += 1

    def drawPixel(self, x: int, pos: tuple):
        if (pos[0] in [x - 1, x, x + 1]):
            self._screen[pos[1]][pos[0]] = 1
        else:
            self._screen[pos[1]][pos[0]] = 0

    def getPixel(self, pos: tuple) -> str:
        if (self._screen[pos[1]][pos[0]] == 1):
            return "#"
        else:
            return "."

    def getScreen(self) -> str:
        screen = ""
        for i in range(self._screenHeight):
            line = ""
            for j in range(self._screenWidth):
                line = line + self.getPixel((j, i))
            screen = screen + line + "\n"
        return screen
            

