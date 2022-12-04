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

    if s1 <= s2 and e1 >= e2:
        total += 1
    elif s2 <= s1 and e2 >= e1:
        total += 1

print(total)
