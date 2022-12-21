#!/usr/bin/python3

import re

read_sample = 0
filename = ["input.txt", "sample.txt"][read_sample]
lines = open(filename).read().strip().split('\n')

monkeys = {}
todo = {}
for line in lines:
    match = re.match(r'(.+): (\d+)', line)
    if match is not None:
        name, val = match.groups()
        monkeys[name] = int(val)
    else:
        name, m1, op, m2 = re.match(r'(.+): (.+) ([+-/*]) (.+)', line).groups()
        todo[name] = (m1, m2, op)

while 'root' not in monkeys:
    to_remove = []
    for name, (m1, m2, op) in todo.items():
        if m1 in monkeys and m2 in monkeys:
            to_remove.append(name)
            if op == '+':
                monkeys[name] = monkeys[m1] + monkeys[m2]
            elif op == '*':
                monkeys[name] = monkeys[m1] * monkeys[m2]
            elif op == '-':
                monkeys[name] = monkeys[m1] - monkeys[m2]
            elif op == '/':
                div, rem = divmod(monkeys[m1], monkeys[m2])
                assert rem == 0
                monkeys[name] = div
            else:
                print("Unrecognized operation")

    for x in to_remove:
        todo.pop(x)

print(monkeys['root'])
