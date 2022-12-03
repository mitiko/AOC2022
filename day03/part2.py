#!/usr/bin/python3

read_sample = 0
filename = ["input.txt", "sample.txt"][read_sample]
lines = open(filename).read().strip().split('\n')

def prio(x):
    if x.islower():
        return 1 + ord(x) - ord('a')
    return 27 + ord(x) - ord('A')

total = 0

for i in range(0, len(lines), 3):
    g3 = lines[i:i+3]
    x, = set(g3[0]) & set(g3[1]) & set(g3[2])
    total += prio(x)

print(total)
