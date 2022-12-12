#!/usr/bin/python3

read_sample = 0
filename = ["input.txt", "sample.txt"][read_sample]
lines = open(filename).read().strip().split('\n')

class Node():
    def __init__(self, level, coord):
        self.level = level
        self.coord = coord
        self.adj = []
    
    def add(self, node):
        self.adj.append(node)

y_len = len(lines)
x_len = len(lines[0])
grid = [[None] * x_len for _ in range(y_len)]
source, target = None, None
Q = set()
count = y_len * x_len
max_distance = count + 100
dist, prev = {}, {}

# connect graph
for y, line in enumerate(lines):
    for x, char in enumerate(line):
        level = ord(char) - ord('a')
        if char == 'S':
            level = ord('a') - ord('a')
        elif char == 'E':
            level = ord('z') - ord('a')

        node = Node(level, (x, y))
        grid[y][x] = node

        if y != 0:
            up = grid[y-1][x]

            if node.level >= up.level - 1:
                node.add(up)
            if up.level >= node.level - 1:
                up.add(node)
        if x != 0:
            left = grid[y][x-1]
            if node.level >= left.level - 1:
                node.add(left)
            if left.level >= node.level - 1:
                left.add(node)
        
        if char == 'S':
            source = node
        elif char == 'E':
            target = node

        Q.add(node)
        dist[node] = max_distance
        prev[node] = None

# perform djikstra
dist[source] = 0
while len(Q) != 0:
    u = min(Q, key = lambda x: dist[x])
    if u == target:
        print("found")
        break
    Q.remove(u)

    for v in u.adj:
        if v not in Q: continue
        alt = dist[u] + 1
        if alt < dist[v]:
            dist[v] = alt
            prev[v] = u

S = []
cnt = 0
u = target
if u == source or prev[u] != None:
    while u != None:
        cnt += 1
        u = prev[u]

print(cnt - 1)

