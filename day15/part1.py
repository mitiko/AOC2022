#!/usr/bin/pypy3

import re
read_sample = 0
filename = ["input.txt", "sample.txt"][read_sample]
lines = open(filename).read().strip().split('\n')

def dist(a, b, x, y):
    return abs(x-a) + abs(y-b)

arr = []
beacons = set()
x_max = 0
x_min = 0

for line in lines:
    matches = re.findall(r'Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)', line)[0]
    # r = [int(t) for t in matches]; print(r)
    sx, sy, x, y = [int(t) for t in matches]
    d = dist(sx, sy, x, y)
    x_max = max(x_max, sx+d, sx-d, x+d, x-d)
    x_min = min(x_min, sx+d, sx-d, x+d, x-d)
    arr.append((sx, sy, dist(sx, sy, x, y)))
    beacons.add((x, y))

print(x_max, x_min)
row = 10 if read_sample == 1 else 2000000
total = 0

for i in range(x_min, x_max):
    in_range = False
    for sx, sy, dd in arr:
        d = dist(sx, sy, i, row)
        if d <= dd:
            # print(f"Sensed ({i}, {row}) by ({sx}, {sy})")
            in_range = True
            break

    # print(i, in_range)
    if in_range:
        if (i, row) in beacons:
            continue
        total += 1
        
print(total)


