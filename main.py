import msvcrt
import sys

f = open(sys.argv[1], "r")
prg = f.read()
f.close()

prgPos = 0

mem = [0]
memPos = 0
commands = [">", "<", "+", "-", "[", "]", ".", ","]

while prgPos < len(prg):
    if prg[prgPos] == ">":
        memPos += 1
        if len(mem) <= memPos: mem.append(0)
    elif prg[prgPos] == "<":
        memPos -= 1
        if memPos < 0:
            print("Cannot Have Negative Cell Pointer")
            sys.exit(0)
    elif prg[prgPos] == "+":
        mem[memPos] += 1
        if mem[memPos] >= 255: mem[memPos] = 0
    elif prg[prgPos] == "-":
        mem[memPos] -= 1
        if mem[memPos] < 0: mem[memPos] = 255
    elif prg[prgPos] == ".": print(chr(mem[memPos]), end='')
    elif prg[prgPos] == ",":
        char = msvcrt.getch()
        if char.decode() == '\r': mem[memPos] = 0
        else: mem[memPos] = ord(char)
    elif prg[prgPos] == "[":
        if mem[memPos] == 0:
            countOpened = 0
            prgPos += 1
            while prgPos < len(prg):
                if prg[prgPos] == "]" and countOpened == 0: break
                elif prg[prgPos] == "[": countOpened += 1
                elif prg[prgPos] == "]": countOpened -= 1
                prgPos += 1
    elif prg[prgPos] == "]":
        if mem[memPos] != 0:
            countClosed = 0
            prgPos -= 1
            while prgPos >= 0:
                if prg[prgPos] == "[" and countClosed == 0: break
                elif prg[prgPos] == "]": countClosed += 1
                elif prg[prgPos] == "[": countClosed -= 1
                prgPos -= 1
    if len(sys.argv) >= 3 and "-s" in sys.argv and prg[prgPos] in commands:
        temp = []
        for i in range(len(mem)):
            if i == memPos:
                temp.append(">"+"0"*(3-len(str(mem[i])))+str(mem[i])+"<")
            else:
                temp.append(" "+"0"*(3-len(str(mem[i])))+str(mem[i])+" ")
        print("\t", prg[prgPos], '['+', '.join(temp)+']', end="")
        inp = input()
        if inp.lower() == "exit": exit(0)
    prgPos += 1
if len(sys.argv) >= 3 and "-e" in sys.argv:
    temp = []
    for i in range(len(mem)):
        if i == memPos:
            temp.append(">" + "0" * (3 - len(str(mem[i]))) + str(mem[i]) + "<")
        else:
            temp.append(" " + "0" * (3 - len(str(mem[i]))) + str(mem[i]) + " ")
    print('['+', '.join(temp)+']')
sys.exit(mem[memPos])
