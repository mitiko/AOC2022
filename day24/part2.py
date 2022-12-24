#!/usr/bin/python3

read_sample = 0
filename = ["input.txt", "sample.txt", "smol.txt"][read_sample]
lines = open(filename).read().strip().split('\n')
def unreachable(): return False

x_max = len(lines[0]) - 2
y_max = len(lines) - 2

blizzards = {}
bliz = { '>': 1, 'v': 2, '<': 4, '^': 8 }
bliz_inv = ['.']
for t in range(1, 16):
    b0 = (t & 1) > 0; b1 = (t & 2) > 0
    b2 = (t & 4) > 0; b3 = (t & 8) > 0
    mapto = ''
    if b0: mapto += '>'
    if b1: mapto += 'v'
    if b2: mapto += '<'
    if b3: mapto += '^'
    bliz_inv.append(mapto)

for y, line in enumerate(lines[1:-1]):
    for x, ch in enumerate(line[1:-1]):
        if ch != '.':
            blizzards[x, y] = bliz[ch]

def bliz_next(bl, x, y):
    if bl == '>': nx, ny = x+1, y
    elif bl == 'v': nx, ny = x, y+1
    elif bl == '<': nx, ny = x-1, y
    elif bl == '^': nx, ny = x, y-1
    else: assert unreachable()

    if nx < 0: nx = x_max-1
    elif nx >= x_max: nx=0

    if ny < 0: ny = y_max-1
    elif ny >= y_max: ny=0

    return nx, ny

def step_blizzards():
    global blizzards
    new_blizzards = {}
    for ((x,y), blc) in blizzards.items():
        for bl in bliz_inv[blc]:
            nx, ny = bliz_next(bl, x, y)
            if (nx, ny) not in new_blizzards:
                new_blizzards[nx, ny] = bliz[bl]
            else:
                new_blizzards[nx, ny] |= bliz[bl]
    blizzards = new_blizzards

start = (0, -1)
goal = (x_max-1, y_max)

bfs = set(); bfs.add(start)
curr_step = 0
while True:
    new_bfs = set()
    found = False
    for pos in bfs:
        x, y = pos
        for next_pos in [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]:
            if next_pos == goal: found = True; break
            if next_pos[0] <= -1 or next_pos[0] >= x_max: continue
            if next_pos[1] <= -1 or next_pos[1] >= y_max: continue
            if next_pos in blizzards: continue
            new_bfs.add(next_pos)

        if found: break # i hate python doesn't have labels on loops
        if pos not in blizzards: # this does not enforce a move
            new_bfs.add(pos)

    # make step
    if found: break
    step_blizzards()
    curr_step += 1
    bfs = new_bfs

trip1 = curr_step

start, goal = goal, start
bfs = set(); bfs.add(start)
curr_step = 0
while True:
    new_bfs = set()
    found = False
    for pos in bfs:
        x, y = pos
        for next_pos in [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]:
            if next_pos == goal: found = True; break
            if next_pos[0] <= -1 or next_pos[0] >= x_max: continue
            if next_pos[1] <= -1 or next_pos[1] >= y_max: continue
            if next_pos in blizzards: continue
            new_bfs.add(next_pos)

        if found: break # i hate python doesn't have labels on loops
        if pos not in blizzards: # this does not enforce a move
            new_bfs.add(pos)

    # make step
    if found: break
    step_blizzards()
    curr_step += 1
    bfs = new_bfs

trip2 = curr_step


start, goal = goal, start
bfs = set(); bfs.add(start)
curr_step = 0
while True:
    new_bfs = set()
    found = False
    for pos in bfs:
        x, y = pos
        for next_pos in [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]:
            if next_pos == goal: found = True; break
            if next_pos[0] <= -1 or next_pos[0] >= x_max: continue
            if next_pos[1] <= -1 or next_pos[1] >= y_max: continue
            if next_pos in blizzards: continue
            new_bfs.add(next_pos)

        if found: break # i hate python doesn't have labels on loops
        if pos not in blizzards: # this does not enforce a move
            new_bfs.add(pos)

    # make step
    if found: break
    step_blizzards()
    curr_step += 1
    bfs = new_bfs

trip3 = curr_step

# WET (https://en.wikipedia.org/wiki/Don%27t_repeat_yourself#WET)
print(trip1 + trip2 + trip3)
