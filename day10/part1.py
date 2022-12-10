#!/usr/bin/python3

read_sample = 0
filename = ["input.txt", "sample.txt"][read_sample]
lines = open(filename).read().strip().split('\n')

class Machine:
    def __init__(self):
        self.cycles = 0
        self.reg = 1

    def exec(self, func):
        if func != None:
            func(self)
    
    def run(self, command, func = None):
        ops = command.split(" ")
        instr = ops[0]
        if instr == "noop":
            self.cycles += 1; self.exec(func)
        elif instr == "addx":
            self.cycles += 1; self.exec(func)
            self.cycles += 1; self.exec(func)
            self.reg += int(ops[1])
        else:
            print("Unrecognized instruction")

total = 0
def interim(m: Machine):
    global total
    if m.cycles in [20, 60, 100, 140, 180, 220]:
        total += m.cycles * m.reg

m = Machine()
for line in lines:
    m.run(line, interim)

print(total)
