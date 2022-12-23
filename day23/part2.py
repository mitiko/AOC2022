#!/usr/bin/python3

read_sample = 0
filename = ["input.txt", "sample.txt", "smol.txt"][read_sample]
lines = open(filename).read().strip().split('\n')

elves = set()

for y, line in enumerate(lines):
    elves.update([(x,y) for x, e in enumerate(line) if e == '#'])

step = 0
while True:
    propositions = {}
    new_elves = set()
    i = step % 4
    step += 1
    for elf in elves:
        x, y = elf
        north_check = [(x, y-1), (x-1, y-1), (x+1, y-1)]
        south_check = [(x, y+1), (x-1, y+1), (x+1, y+1)]
        west_check = [(x-1, y), (x-1, y-1), (x-1, y+1)]
        east_check = [(x+1, y), (x+1, y-1), (x+1, y+1)]
        check = [item for sublist in [north_check, south_check, west_check, east_check] for item in sublist]

        # stationary end goal
        if all([x not in elves for x in check]):
            new_elves.add(elf)
            continue

        if i == 0 and all([x not in elves for x in north_check]):
            propositions[elf] = (x, y-1)
            continue

        if i <= 1 and all([x not in elves for x in south_check]):
            propositions[elf] = (x, y+1)
            continue

        if i <= 2 and all([x not in elves for x in west_check]):
            propositions[elf] = (x-1, y)
            continue

        if i <= 3 and all([x not in elves for x in east_check]):
            propositions[elf] = (x+1, y)
            continue

        # secondary checks to emulate the list wrapping around
        if all([x not in elves for x in north_check]):
            propositions[elf] = (x, y-1)
            continue

        if all([x not in elves for x in south_check]):
            propositions[elf] = (x, y+1)
            continue

        if all([x not in elves for x in west_check]):
            propositions[elf] = (x-1, y)
            continue

        if all([x not in elves for x in east_check]):
            propositions[elf] = (x+1, y)
            continue

        new_elves.add(elf)
        # else no move..

    # invert dictionary
    tmp = {}
    for k, v in propositions.items():
        if v not in tmp: tmp[v] = [k]
        else: tmp[v].append(k)

    for k, v in tmp.items():
        if len(v) == 1:
            new_elves.add(k)
        else:
            new_elves.update(v)

    if len(elves & new_elves) == len(elves):
        break
    elves = new_elves

print(step)
