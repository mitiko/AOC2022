#!/usr/bin/python3

import re

read_sample = 0
filename = ["input.txt", "sample.txt"][read_sample]
lines = open(filename).read().split('\n')

def flatten(x): return [item for sublist in x for item in sublist]

if read_sample == 1:
    stacks = [[] for _ in range(3)]
    max_height = 3
else:
    stacks = [[] for _ in range(9)]
    max_height = 8

for line in lines[:max_height]:
    for i in range(0, len(line), 4):
        container = re.findall("\[(.)\]", line[i:i+4])
        if len(container) != 0:
            stacks[i//4].append(container[0])

for stack in stacks:
    stack.reverse()

for line in lines[max_height+2:]:
    t = re.findall("\d+", line)

    count = int(t[0])
    # make 0-index
    source = int(t[1])-1
    dest = int(t[2])-1

    temp = []
    for i in range(count):
        container = stacks[source].pop()
        temp.append(container)

    for i in range(count):
        stacks[dest].append(temp.pop())

output = ""
for stack in stacks:
    if len(stack) != 0:
        output += stack.pop()

print(output)
