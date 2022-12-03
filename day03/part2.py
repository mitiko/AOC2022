#!/usr/bin/python3

read_sample = 0
filename = ["input.txt", "sample.txt"][read_sample]
input = open(filename).readlines()

total = 0
g3 = []

for line in input:
    t = line.rsplit()[0]
    g3.append(t)
    if len(g3) != 3:
        continue

    x, y, z = set(g3[0][:]), set(g3[1][:]), set(g3[2][:])
    for v in x:
        if v in y:
            if v in z:
                if v.islower():
                    prio = 1 + ord(v) - ord('a')
                else:
                    prio = 27 + ord(v) - ord('A')
                total += prio

    g3 = []

print(total)
