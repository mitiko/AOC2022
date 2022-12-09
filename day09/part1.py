#!/usr/bin/python3

read_sample = 0
filename = ["input.txt", "sample.txt"][read_sample]
lines = open(filename).read().strip().split('\n')

def move(head, tail, d):
    hx, hy = head
    tx, ty = tail
    if d == 'R':
        hx += 1
    elif d == 'L':
        hx -= 1
    elif d == 'D':
        hy -= 1
    elif d == 'U':
        hy += 1
    else:
        print("Unrecognized direction"); assert False
    
    taxicab_distance = abs(hx-tx) + abs(hy-ty)
    assert taxicab_distance <= 3

    if taxicab_distance == 2:
        if hx == tx + 2: # direction = R
            tx += 1
        elif hx == tx - 2: # direction L
            tx -= 1
        elif hy == ty - 2: # direction D
            ty -= 1
        elif hy == ty + 2: # direction U
            ty += 1
        else: pass # diagonal is fine
    elif taxicab_distance == 3:
        if hx == tx + 2:
            tx += 1
            if hy == ty - 1: ty -= 1
            else: ty += 1
        elif hx == tx - 2:
            tx -= 1
            if hy == ty + 1: ty += 1
            else: ty -= 1
        elif hx == tx + 1:
            tx += 1
            if hy == ty + 2: ty += 1
            else: ty -= 1
        elif hx == tx - 1:
            tx -= 1
            if hy == ty - 2: ty -= 1
            else: ty += 1
        else: assert False
    return ((hx, hy), (tx, ty))

head = (0, 0)
tail = (0, 0)
visited = set()


for line in lines:
    [direction, steps] = line.split(" ")
    steps = int(steps)

    for i in range(steps):
        head, tail = move(head, tail, direction)
        visited.add(tail)

print(len(visited))
