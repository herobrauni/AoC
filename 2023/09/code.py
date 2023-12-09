# Advent of code Year 2023 Day 9 solution
# Author = brauni
# Date = 2023-12-09
"https://adventofcode.com/2023/day/9"

import re
from collections import Counter
import copy
import os
import math

solution_1, solution_2 = 0, 0

with open(os.getcwd() + "/AoC_private/2023/09/input.txt", 'r') as f:
# with open(os.getcwd() + "/2023/09/example.txt", "r") as f:
    input = f.read()
    input = input.split("\n")
    input = [re.findall(r"-?\d+", x) for x in input]

# PART 0


print(input)

def diffs(line):
    test = []
    for i in range(1, len(line)):
        test.append(int(line[i]) - int(line[i - 1]))
    return test

# PART 1
hist = {}
for line in input:
    start = input.index(line)
    hist[start] = []
    hist[start].append([int(x) for x in line])
    while True:
        hist[start].append(diffs(line))
        if all([True if x == 0 else False for x in hist[start][-1]]):
            break
        line = hist[start][-1]
    for i in range(len(hist[start]) - 1, 0, -1):
        hist[start][i - 1].append(hist[start][i][-1] + hist[start][i - 1][-1])
        # PART 2
        hist[start][i - 1].insert(0,hist[start][i - 1][0]-hist[start][i][0])

for l in hist:
    solution_1 += hist[l][0][-1]
    solution_2 += hist[l][0][0]

# SOLUTIONS

print("Part One : " + str(solution_1) + "\nPart Two : " + str(solution_2))
