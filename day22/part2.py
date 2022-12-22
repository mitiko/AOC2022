#!/usr/bin/python3

read_sample = 0
filename = ["input.txt", "sample.txt"][read_sample]
notes = open(filename).read().split('\n\n')

puzzle_map = notes[0].split('\n')
path = notes[1]
facing = '^' # first turn right is implicit

face_len = min([len(x) for x in puzzle_map]) # 50 for input

facing_score = {'>': 0, 'V': 1, '<': 2, '^': 3}
facings_clockwise = {'<': '^', '^': '>', '>': 'V', 'V': '<'}
# invert dictionary mapping
facings_anticlockwise = {v: k for k, v in facings_clockwise.items()}

# instr = (dir, steps)
instructions = []
for x in [x.split('L') for x in path.split('R')]:
    instructions.append(('R', int(x[0])))
    for y in x[1:]:
        instructions.append(('L', int(y)))

y = 0
x = len(puzzle_map[0]) - len(puzzle_map[0].lstrip())

# does direction change?
bound_rows = []
bound_cols = []

for row in puzzle_map:
    end = len(row) - 1
    start = len(row) - len(row.lstrip())
    bound_rows.append((start, end))

max_col = max([len(x) for x in puzzle_map])
for col in range(max_col):
    start = 0
    for i in range(len(puzzle_map)):
        if len(puzzle_map[i]) > col and puzzle_map[i][col] != ' ':
            start = i
            break
    end = len(puzzle_map) - 1
    for i in range(start, len(puzzle_map)):
        if len(puzzle_map[i]) > col and puzzle_map[i][col] != ' ':
            end = i
    bound_cols.append((start, end))

def wrap(nx, ny, face):
    # check which face we're on?

    if face == '>':
        if ny < 50: # face 2, wraps to 5 backwards
            nf = '<'
            ny = 149 - ny
            nx = 99
        elif ny < 100: # face 3, wraps to 2 up
            nf = '^'
            nx = ny + 50
            ny = 49
        elif ny < 150: # face 5, wraps to 2 left
            nf = '<'
            ny = 149 - ny
            nx = 149
        else: # face 6, wraps to 5 up
            nf = '^'
            nx = ny - 100
            ny = 149
    elif face == '<':
        if ny < 50: # face 1, wraps to 4 backwards
            nf = '>'
            ny = 149 - ny
            nx = 0
        elif ny < 100: # face 3, wraps to 4 down
            nf = 'V'
            nx = ny - 50
            ny = 100
        elif ny < 150: # face 4, wraps to 1 bacwards
            nf = '>'
            ny = 149 - ny
            nx = 50
        else: # face 6, wraps to 1 down
            nf = 'V'
            nx = ny - 100
            ny = 0
    elif face == 'V':
        if nx < 50: # face 6, wraps to 2 down
            nf = 'V'
            nx = nx + 100
            ny = 0
        elif nx < 100: # face 5, wraps to 6 left
            nf = '<'
            ny = nx + 100
            nx = 49
        else: # face 2, wraps to 3 left
            nf = '<'
            ny = nx - 50
            nx = 99
    elif face == '^':
        if nx < 50: # face 4, wraps to 3 right
            nf = '>'
            ny = nx + 50
            nx = 50
        elif nx < 100: # face 1, wraps to 6 right
            nf = '>'
            ny = nx + 100
            nx = 0
        else: # face 2, wraps to 6 up
            nf = '^'
            nx = nx - 100
            ny = 199

    return nx, ny, nf

def next_pos():
    global facing
    global x, y
    nx, ny = x, y
    if facing == '>':
        nx += 1
    elif facing == 'V':
        ny += 1
    elif facing == '<':
        nx -= 1
    elif facing == '^':
        ny -= 1

    nf = facing
    # is out of bounds
    if x == nx:
        start, end = bound_cols[x]
        if ny < start or ny > end:
            nx, ny, nf = wrap(nx, ny, facing)
    elif y == ny:
        start, end = bound_rows[y]
        if nx < start or nx > end:
            nx, ny, nf = wrap(nx, ny, facing)
    
    return nx, ny, nf

def move(instr):
    global facing
    global x, y
    dir, steps = instr

    if dir == 'R':
        facing = facings_clockwise[facing]
    elif dir == 'L':
        facing = facings_anticlockwise[facing]

    # move x steps...
    for _ in range(steps):
        nx, ny, nf = next_pos()
        # check if wall
        if puzzle_map[ny][nx] == '#':
            break
        x, y, facing = nx, ny, nf

for instr in instructions:
    move(instr)

print(1000 * (y + 1) + 4 * (x + 1) + facing_score[facing])
