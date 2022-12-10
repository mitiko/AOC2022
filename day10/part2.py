#!/usr/bin/python3

read_sample = 0
filename = ["input.txt", "sample.txt"][read_sample]
lines = open(filename).read().strip().split('\n')

cycles = 0
reg = 1
# crt = [[0]*40 for _ in range(6)]
crt = [0]*240
pos = 0

def render(reg):
    global crt
    global pos
    sprite = [reg-1, reg, reg+1]

    if pos%40 in sprite:
        crt[pos] = 1
    else:
        crt[pos] = 0

    pos += 1

for line in lines:
    opperands = line.split(" ")

    instr = opperands[0]
    val = reg

    if instr == "noop":
        cycles += 1
    elif instr == "addx":
        cycles += 1

    render(reg)

    if instr == "addx":
        cycles += 1
        render(reg)
        V = int(opperands[1])
        reg += V

for i in range(6):
    for j in range(40):
        pixel = crt[i*40 + j]
        if pixel == 0:
            print('.', end="")
        elif pixel == 1:
            print('#', end="")
    print()
