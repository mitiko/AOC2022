#!/usr/bin/python3

input = open("input.txt").readlines()

max_calories = None
accum_calories = 0

for line in input:
    if line == "\n":
        if max_calories == None or accum_calories > max_calories:
            max_calories = accum_calories
        accum_calories = 0
        continue

    calories = int(line)
    accum_calories += calories

if max_calories == None or accum_calories > max_calories:
    max_calories = accum_calories

print(max_calories)
