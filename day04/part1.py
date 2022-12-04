#!/usr/bin/python3

read_sample = 0
filename = ["input.txt", "sample.txt"][read_sample]
lines = open(filename).read().strip().split('\n')

def flatten(x): return [item for sublist in x for item in sublist]

total = 0
for line in lines:
    t = [s.split('-') for s in line.split(',')]
    t = [int(s) for s in flatten(t)]
    [s1, e1, s2, e2] = t

    if (s1 <= s2 and e1 >= e2) or \
        (s2 <= s1 and e2 >= e1):
        total += 1

print(total)
