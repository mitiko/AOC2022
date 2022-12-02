#!/usr/bin/python3

input = open("input.txt").readlines()
# rock -> A
# paper -> B
# scissors -> C
# A -> 1, B -> 2, C -> 3
# X -> 0, Y -> 1, Z -> 2
# loose: 0, draw: 3, win: 6

#  loose, draw, win
# A -> [3, 1, 2]
# B -> [1, 2, 3]
# C -> [2, 3, 1]
choice_matrix = [
    [3, 1, 2],
    [1, 2, 3],
    [2, 3, 1],
]
def score(x, y):
    x_idx = ord(x) - ord('A')
    y_idx = ord(y) - ord('X')
    win_points = [0, 3, 6][y_idx] # y_idx * 3

    choice_points = choice_matrix[x_idx][y_idx]
    return choice_points + win_points

total = 0
for line in input:
    [them, me] = line.rsplit()
    total += score(them, me)

print(total)
