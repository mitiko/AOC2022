#!/usr/bin/python3

read_sample = 0
filename = ["input.txt", "sample.txt"][read_sample]
lines = open(filename).read().strip().split('\n')

idx = set()
total = 0

for i in range(len(lines)):
    line = lines[i]

    # scan left
    prev = -1
    for j in range(len(line)):
        loc = (i, j)
        tree = int(lines[i][j])

        if tree <= prev: continue
        prev = tree
        if not loc in idx:
            total += 1
            idx.add(loc)

    # scan right
    prev = -1
    for j in reversed(range(len(line))):
        loc = (i, j)
        tree = int(lines[i][j])

        if tree <= prev: continue
        prev = tree
        if not loc in idx:
            total += 1
            idx.add(loc)

# scan down
for j in range(len(lines[0])):
    prev = -1
    for i in range(len(lines)):
        loc = (i, j)
        tree = int(lines[i][j])

        if tree <= prev: continue
        prev = tree
        if loc not in idx:
            total += 1
            idx.add(loc)

# scan up
for j in range(len(lines[0])):
    prev = -1
    for i in reversed(range(len(lines))):
        loc = (i, j)
        tree = int(lines[i][j])

        if tree <= prev: continue
        prev = tree
        if loc not in idx:
            total += 1
            idx.add(loc)

print(total)
