#!/usr/bin/python3

read_sample = 0
filename = ["input.txt", "sample.txt"][read_sample]
lines = open(filename).read().strip().split('\n')

total = 0
cycles = 0
reg = 1
done = set()

def do_check(c, r):
    global total
    for kk in [20, 60, 100, 140, 180, 220]:
        if kk in done: continue
        if c >= kk:
            total += kk*r
            done.add(kk)
            break

for line in lines:
    opperands = line.split(" ")
    instr = opperands[0]

    if instr == "noop":
        cycles += 1
    elif instr == "addx":
        cycles += 1
    do_check(cycles, reg)

    if instr == "addx":
        cycles += 1
        do_check(cycles, reg)
    if instr == "addx":
        V = int(opperands[1])
        reg += V

print(total)
