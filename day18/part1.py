#!/usr/bin/python3

read_sample = 0
filename = ["input.txt", "sample.txt"][read_sample]
lines = open(filename).read().strip().split('\n')

ss = set()

for line in lines:
    [x,y,z] = [int(t) for t in line.split(',')]
    ss.add((x,y,z))

total = 0
for cube in ss:
    x,y,z = cube
    # check if cubes next to it are in set
    for next in [(x+1,y,z), (x-1,y,z), (x,y+1,z), (x,y-1,z), (x,y,z+1), (x,y,z-1)]:
        if not next in ss:
            total += 1

print(total)
