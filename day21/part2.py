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

not_dep = set()
dep = set()
bfs = [('root', [])]
humn_count = 0
while len(bfs) > 0:
    name, path = bfs[0]; bfs = bfs[1:]
    if name == 'humn':
        humn_count += 1
        dep.update(path)
        continue
    if name in monkeys:
        continue

    m1, m2, _ = todo[name]
    p = path.copy()
    p.append(name)

    bfs.append((m1, p))
    bfs.append((m2, p.copy()))

assert humn_count == 1
monkeys.pop('humn')
not_dep = set(todo.keys()) - dep

def div_exact(a, b):
    div, rem = divmod(a, b)
    assert rem == 0
    return div

while len(not_dep) > 0:
    to_remove = set()
    for name in not_dep:
        m1, m2, op = todo[name]
        if m1 in monkeys and m2 in monkeys:
            to_remove.add(name)
            if op == '+':
                monkeys[name] = monkeys[m1] + monkeys[m2]
            elif op == '*':
                monkeys[name] = monkeys[m1] * monkeys[m2]
            elif op == '-':
                monkeys[name] = monkeys[m1] - monkeys[m2]
            elif op == '/':
                monkeys[name] = div_exact(monkeys[m1], monkeys[m2])
            else:
                print("Unrecognized operation")
    not_dep = not_dep - to_remove

def equalize(name, val):
    if name == 'humn':
        print('humn:', val)
        return
    m1, m2, op = todo[name]
    if op == '+':
        if m1 in monkeys:
            return equalize(m2, val - monkeys[m1])
        else:
            return equalize(m1, val - monkeys[m2])
    elif op == '*':
        if m1 in monkeys:
            return equalize(m2, div_exact(val, monkeys[m1]))
        else:
            return equalize(m1, div_exact(val, monkeys[m2]))
    elif op == '-':
        if m1 in monkeys:
            return equalize(m2, monkeys[m1] - val)
        else:
            return equalize(m1, monkeys[m2] + val)
    elif op == '/':
        if m1 in monkeys:
            return equalize(m2, div_exact(monkeys[m1], val))
        else:
            return equalize(m1, monkeys[m2] * val)
    else:
        print("Unrecognized operation")
    
m1, m2, _ = todo['root']
if m1 in monkeys:
    equalize(m2, monkeys[m1])
else:
    equalize(m1, monkeys[m2])