#!/usr/bin/python3

read_sample = 0
filename = ["input.txt", "sample.txt"][read_sample]
lines = open(filename).read().strip().split('\n')

def nnext(t: tuple):
    x,y,z = t
    return [(x+1,y,z), (x-1,y,z), (x,y+1,z), (x,y-1,z), (x,y,z+1), (x,y,z-1)]

cubes = set()

for line in lines:
    [x,y,z] = [int(t) for t in line.split(',')]
    cubes.add((x,y,z))

ext_cubes = set()
bfs = [(-1, -1, - 1)]
ext_cubes.add(bfs[0])

def out_of_bounds(cube):
    x, y, z = cube
    # return (x > 50 or y > 50 or z > 50) or (x < -1 or y < -1 or z < -1)
    return (x > 22 or y > 22 or z > 22) or (x < -1 or y < -1 or z < -1)

while len(bfs) > 0:
    node = bfs[0]; bfs = bfs[1:]
    for cc in nnext(node):
        if out_of_bounds(cc): continue
        if cc in cubes or cc in ext_cubes:
            continue
        bfs.append(cc)
        ext_cubes.add(cc)

total = 0
for ext in ext_cubes:
    for tt in nnext(ext):
        if tt in cubes:
            total += 1

print(total)
