#!/usr/bin/python3

read_sample = 0
filename = ["input.txt", "sample.txt"][read_sample]
lines = open(filename).read().strip().split('\n')

total = 0

# scan inner block only
for i in range(1, len(lines)-1):
    for j in range(1, len(lines[0])-1):
        line = lines[i]
        tree = int(line[j])

        score_left = 0
        score_right = 0
        score_down = 0
        score_up = 0

        left = [int(x) for x in line[:j]]
        right = [int(x) for x in line[j+1:]]
        down = [int(x[j]) for x in lines[:i]]        
        up = [int(x[j]) for x in lines[i+1:]]        

        vis = -1
        for x in reversed(left):
            if x > vis:
                vis = x
            score_left += 1
            if tree <= vis:
                break

        vis = -1
        for x in right:
            if x > vis:
                vis = x
            score_right += 1
            if tree <= vis:
                break

        vis = -1
        for x in reversed(down):
            if x > vis:
                vis = x
            score_down += 1
            if tree <= vis:
                break

        vis = -1
        for x in up:
            if x > vis:
                vis = x
            score_up += 1
            if tree <= vis:
                break
        
        total_score = score_left * score_right * score_up * score_down

        if total_score > total:
            total = total_score

print(total)
