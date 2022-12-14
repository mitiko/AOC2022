#!/usr/bin/python3

read_sample = 0
filename = ["input.txt", "sample.txt"][read_sample]
lines = open(filename).read().strip().split('\n')

x_len = 86
y_len = 184
x_norm = 488
grid = [['.']*x_len for _ in range(y_len)]

if read_sample == 1:
    x_len = 11
    y_len = 10
    x_norm = 493

for line in lines:
    coords = [a.split(",") for a in line.split("->")]
    path = [(int(x), int(y)) for [x,y] in coords]
    for i in range(len(path) - 1):
        sx = path[i][0] - x_norm
        ex = path[i+1][0] - x_norm
        sy = path[i][1]
        ey = path[i+1][1]
        sx, ex = min(sx, ex), max(sx, ex)
        sy, ey = min(sy, ey), max(sy, ey)

        for y in range(sy, ey+1):
            for x in range(sx, ex+1):
                grid[y][x] = '#'

def print_cave():
    global grid
    for ss in grid:
        for xx in ss:
            print(xx, end='')
        print()

sand_count = 0
while True:
    # new sand particle
    sand_x = 500 - x_norm
    sand_y = 0
    out_of_boundary = False

    # falling loop
    while True:
        # check which of 3 possible places it can go
        # if none, then break
        # if placed out of boundaries, then break outer
        if sand_y == y_len - 1 or sand_x == 0 or sand_x == x_len:
            out_of_boundary = True
            break

        under = grid[sand_y + 1]
        if sand_x == 0:
            next_bl = [under[sand_x], under[sand_x + 1]]
        elif sand_x == x_len - 1:
            next_bl = [under[sand_x], under[sand_x - 1]]
        else:
            next_bl = [under[sand_x], under[sand_x - 1], under[sand_x + 1]]
        
        moving = False
        for i in range(len(next_bl)):
            if next_bl[i] != '.': continue
            
            moving = True
            found = i
            sand_y += 1
            if i == 1 and sand_x == 0:
                sand_x = sand_x + 1
            elif i != 0:
                sand_x += 2 * i - 3
            break

        if not moving:
            grid[sand_y][sand_x] = 'o'
            break

    if out_of_boundary:
        break
    sand_count += 1

print(sand_count)
