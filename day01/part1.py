#!/usr/bin/python3

input = open("input.txt").readlines()

max_calories = 0
accum_calories = 0

for line in input:
    if line == "\n":
        if accum_calories > max_calories:
            max_calories = accum_calories
        accum_calories = 0
        continue

    calories = int(line)
    accum_calories += calories

if accum_calories > max_calories:
    max_calories = accum_calories

print(max_calories)
