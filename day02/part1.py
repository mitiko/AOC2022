#!/usr/bin/python3

input = open("input.txt").readlines()
# rock -> A
# paper -> B
# scissors -> C
# A -> 1, B -> 2, C -> 3
# win: 6, draw: 3, loose: 0


# A -> [3, 6, 0]
# B -> [0, 3, 6]
# C -> [6, 0, 3]
score_matrix = [
    [3, 6, 0],
    [0, 3, 6],
    [6, 0, 3],
]
def score(x, y):
    x_idx = ord(x) - ord('A')
    y_idx = ord(y) - ord('X')
    choice_points = y_idx + 1
    win_points = score_matrix[x_idx][y_idx]
    return choice_points + win_points

total = 0
for line in input:
    [them, me] = line.split('\n')[0].split(' ')
    print(f"'{them}', '{me}'")
    total += score(them, me)

print(total)
