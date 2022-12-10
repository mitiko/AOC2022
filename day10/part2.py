#!/usr/bin/python3

read_sample = 0
filename = ["input.txt", "sample.txt"][read_sample]
lines = open(filename).read().strip().split('\n')

class Machine:
    def __init__(self):
        self.cycles = 0
        self.reg = 1
        self.crt = [0] * 240

    def exec(self, func):
        self.draw()
        if func != None:
            func(self)
    
    def draw(self):
        sprite = [self.reg - 1, self.reg, self.reg + 1]
        pos = self.cycles - 1
        if pos % 40 in sprite:
            self.crt[pos] = 1
        else:
            self.crt[pos] = 0
    
    def render(self):
        for i in range(6):
            for j in range(40):
                pixel = self.crt[i * 40 + j]
                if pixel == 1:
                    print('#', end="")
                else:
                    print('.', end="")
            print()

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

m = Machine()
for line in lines:
    m.run(line)

m.render()
