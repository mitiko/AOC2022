#!/usr/bin/python3

read_sample = 0
filename = ["input.txt", "sample.txt"][read_sample]
lines = open(filename).read().split('\n')

line = lines[0]
for i in range(len(line)-4):
    span = line[i:i+4]
    if len(set(span)) == 4:
        print(i+4)
        break
