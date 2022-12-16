#!/usr/bin/pypy3

import re
read_sample = 0
filename = ["input.txt", "sample.txt"][read_sample]
lines = open(filename).read().strip().split('\n')

def dist(a, b, x, y):
    return abs(x-a) + abs(y-b)

arr = []
beacons = set()

for line in lines:
    matches = re.findall(r'Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)', line)[0]
    # r = [int(t) for t in matches]; print(r)
    sx, sy, x, y = [int(t) for t in matches]
    d = dist(sx, sy, x, y)
    # x_max = max(x_max, sx+d, sx-d, x+d, x-d)
    # x_min = min(x_min, sx+d, sx-d, x+d, x-d)
    arr.append((sx, sy, dist(sx, sy, x, y)))
    beacons.add((x, y))


if read_sample == 1:
    x_min, x_max = 0, 20
    y_min, y_max = 0, 20
else:
    x_min, x_max = 0, 4000000
    y_min, y_max = 0, 4000000

# i = x_min

def is_covered(x, y):
    for sx, sy, dd in arr:
        if dist(sx, sy, x, y) <= dd:
            return True
    return False

for sx, sy, dd in arr:
    # check perimeter
    r1 = min(y_max, max(y_min, sy - dd))
    r2 = min(y_max, max(y_min, sy + dd))
    # print(r1, r2)
    for r in range(r1, r2):
        # get right x
        k = sx + (dd - abs(sy - r)) + 1
        if k < x_min or k > x_max:
            continue
        # print(k, r)
        if not is_covered(k, r):
            print(k, r)
