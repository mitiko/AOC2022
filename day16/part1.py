#!/usr/bin/pypy3

import re
read_sample = 0
filename = ["input.txt", "sample.txt"][read_sample]
lines = open(filename).read().strip().split('\n')

rates = {}
nnext = {}
nprev = {}

midx = {'AA': 0}
arr = []

for line in lines:
    valve, rate, next = re.findall(r'^Valve ([A-Z]{2}) has flow rate=(\d+); tunnels? leads? to valves? (.+)$', line)[0]
    rate = int(rate)
    next = [x.strip() for x in next.split(',')]
    print(valve, rate, next)
    rates[valve] = rate
    nnext[valve] = next
    for n in next:
        if n in nprev:
            nprev[n].append(valve)
        else:
            nprev[n] = [valve]
    if rate > 0:
        midx[valve] = len(midx)
        arr.append(valve)

def bfs_search(curr, end):
    depth = 0
    while True:
        next = set()
        for x in curr:
            if x == end:
                return depth
            for y in nnext[x]:
                next.add(y)
        curr = next
        depth += 1

# compute the shortest distances where rate > 0
dist = {}
for x in midx.keys():
    for y in midx.keys():
        if x == y: continue
        dist[x,y] = bfs_search([x], y)

print(dist)

def is_set(mask, node):
    return mask & (1 << midx[node]) > 0

def set_bit(mask, node):
    return mask | (1 << midx[node])

best = 0
def search(curr_best, curr, time_left, mask):
    global best
    if curr_best > best:
        best = curr_best

    if time_left <= 0:
        return
    
    if not is_set(mask, curr):
        search(curr_best + rates[curr] * time_left, curr, time_left - 1, set_bit(mask, curr))
        return

    for x in arr:
        if is_set(mask, x): continue
        search(curr_best, x, time_left - dist[curr,x], mask)

search(0, 'AA', 30, 0)
print(best)

