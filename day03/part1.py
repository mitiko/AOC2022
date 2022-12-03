#!/usr/bin/python3

read_sample = 0
filename = ["input.txt", "sample.txt"][read_sample]
input = open(filename).readlines()

total = 0

for line in input:
    t = line.rsplit()[0]
    l = len(t) // 2
    a, b = t[:l], t[l:]
    x, y = set(a[:]), set(b[:])

    # in part2 I found this only works if len(a) == len(b)
    # use x, y = set(a[:]), set(b[:]) instead
    # for c1, c2 in zip(a[:], b[:]):
    #     x.add(c1)
    #     y.add(c2)

    for v in x:
        if v in y:
            if v.islower():
                prio = 1 + ord(v) - ord('a')
            else:
                prio = 27 + ord(v) - ord('A')
            total += prio

print(total)
