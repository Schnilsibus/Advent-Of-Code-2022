from CPU import CPU
from CRT import CRT

import os

def convertInput(input: list) -> list:
    commands = []
    for line in input:
        if (line.endswith("\n")):
            line = line[:-1]
        l = line.split()
        if (len(l) == 1):
            commands.append(l)
        else:
            commands.append([l[0], int(l[1])])
    return commands

def simulateProgramm(programm: list, cyclesOfInterest: list) -> list:
    cpu = CPU()
    strengthsOfInterest = []
    while (cpu.getPC() < len(programm)):
        if (not cpu.hasOP()):
            op = programm[cpu.getPC()]
            if (op[0] == "noop"):
                cpu.nop()
            elif(op[0] == "addx"):
                cpu.addX(op[1])
        if (cpu.getCycle() in cyclesOfInterest):
            strengthsOfInterest.append(cpu.getX() * cpu.getCycle())
        cpu.doCycle()
    return strengthsOfInterest

def renderImage(programm: list) -> str:
    cpu = CPU()
    crt = CRT()
    while (cpu.getPC() < len(programm)):
        if (not cpu.hasOP()):
            op = programm[cpu.getPC()]
            if (op[0] == "noop"):
                cpu.nop()
            elif(op[0] == "addx"):
                cpu.addX(op[1])
        x = cpu.getX()
        cpu.doCycle()
        crt.doCycle(x=x)
    return crt.getScreen()

with open(os.path.dirname(__file__) + "\\input.txt", "r") as file:
    input = file.readlines()
programm = convertInput(input=input)
cyclesOfInterest = [20, 60, 100, 140, 180, 220]
signalStrengths = simulateProgramm(programm=programm, cyclesOfInterest=cyclesOfInterest)
print(f"The sum of the signal strength at the six given cycles is {sum(signalStrengths)}.")
screen = renderImage(programm=programm)
print("The programm produced this screen:")
print(screen)