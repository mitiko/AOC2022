#!/usr/bin/python3

read_sample = 0
filename = ["input.txt", "sample.txt"][read_sample]
lines = open(filename).read().strip().split('\n')

total = 0
for line in lines:
    t = line.split(',')
    s = t[0].split('-')
    s1 = int(s[0])
    e1 = int(s[1])
    s = t[1].split('-')
    s2 = int(s[0])
    e2 = int(s[1])

    if not (e1 < s2 or e2 < s1):
        total += 1

print(total)
