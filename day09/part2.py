#!/usr/bin/python3

read_sample = 0
filename = ["input.txt", "sample2.txt"][read_sample]
lines = open(filename).read().strip().split('\n')

visited = set()

def move_head(head, d):
    hx, hy = head

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

    return (hx, hy)


def move_tail(head, tail):
    hx, hy = head
    tx, ty = tail
    
    taxicab_distance = abs(hx-tx) + abs(hy-ty)

    # since the head may move diagonally now...
    assert taxicab_distance <= 4

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
    elif taxicab_distance == 4:
        if hx == tx + 2:
            tx += 1
            if hy == ty + 2: ty += 1
            else: ty -= 1
        elif hx == tx - 2:
            tx -= 1
            if hy == ty + 2: ty += 1
            else: ty -= 1
        else: assert False
    return (tx, ty)


rope = [(0, 0)]*10
for line in lines:
    [direction, steps] = line.split(" ")
    steps = int(steps)

    for i in range(steps):
        rope[0] = move_head(rope[0], direction)
        for j in range(1, len(rope)):
            rope[j] = move_tail(rope[j-1], rope[j])
        visited.add(rope[9])

print(len(visited))
