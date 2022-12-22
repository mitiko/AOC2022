#!/usr/bin/python3

read_sample = 0
filename = ["input.txt", "sample.txt"][read_sample]
notes = open(filename).read().split('\n\n')

puzzle_map = notes[0].split('\n')
path = notes[1]
facing = '^' # first turn right is implicit

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

wrap_around_rows = []
wrap_around_cols = []

for row in puzzle_map:
    end = len(row) - 1
    start = len(row) - len(row.lstrip())
    wrap_around_rows.append((start, end))

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
    wrap_around_cols.append((start, end))

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

    # is out of bounds
    if x == nx:
        # check horizontal (rows)
        start, end = wrap_around_cols[x]
        if ny < start:
            ny = end
        elif ny > end:
            ny = start
    elif y == ny:
        # check vertical (cols)
        start, end = wrap_around_rows[y]
        if nx < start:
            nx = end
        elif nx > end:
            nx = start
    return nx, ny

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
        nx, ny = next_pos()
        # check if wall
        # if wall -> break
        if puzzle_map[ny][nx] == '#':
            break
        # else -> curr_pos = pos, steps -= 1
        x, y = nx, ny


for instr in instructions:
    move(instr)

print(1000 * (y + 1) + 4 * (x + 1) + facing_score[facing])

