#!/usr/bin/python3

read_sample = 0
filename = ["input.txt", "sample.txt"][read_sample]
lines = open(filename).read().strip().split('\n')

def prio(x):
    if x.islower():
        return 1 + ord(x) - ord('a')
    return 27 + ord(x) - ord('A')

total = 0
for line in lines:
    m = len(line) // 2
    x, = set(line[:m]) & set(line[m:])
    total += prio(x)

print(total)
