# Advent of code Year 2023 Day 11 solution
# Author = brauni
# Date = 2023-12-11
"https://adventofcode.com/2023/day/11"

import re
from collections import Counter
import copy
import os
import math
import numpy as np
import itertools

solution_1, solution_2 = 0, 0

with open(os.getcwd() + "/AoC_private/2023/11/input.txt", 'r') as f:
# with open(os.getcwd() + "/2023/11/example.txt", "r") as f:
    input = f.read()
    input = input.split("\n")
    # input = []
    # for line in f.readlines():
    # input.append(int(line))
    # input = [int(line) for line in f.readlines()]
    # input = [line for line in f.readlines()]

# PART 0


print(input)
input_clean = []
for line in input:
    filler = ["X"] * len(line)
    if all([True if x == "." or x == "X" else False for x in line]):
        # input_clean.append(line)
        input_clean.append(filler)
    else:
        input_clean.append(line)

input_clean_90 = list(zip(*input_clean[::-1]))
input_clean = []
for line in input_clean_90:
    filler = ["X"] * len(line)
    if all([True if x == "." or x == "X" else False for x in line]):
        # input_clean.append(line)
        input_clean.append(filler)
    else:
        input_clean.append(line)

input_clean_finished = list(zip(*input_clean))[::-1]

print(input_clean_finished)
# PART 1

ic = np.array(input_clean_finished)
galaxies = np.where(ic == "#")
galaxies = [(x, galaxies[1][n]) for n, x in enumerate(list(galaxies[0]))]

paths = list(itertools.combinations(galaxies, 2))


for p in paths:
    l = abs(p[0][0] - p[1][0]) + abs(p[0][1] - p[1][1])

    x1 = p[0][0] if p[0][0] < p[1][0] else p[1][0]
    x2 = p[0][0] if p[0][0] >= p[1][0] else p[1][0]
    y1 = p[0][1] if p[0][1] < p[1][1] else p[1][1]
    y2 = p[0][1] if p[0][1] >= p[1][1] else p[1][1]

    z = ic[x1 : x2 + 1, y1 : y2 + 1]

    l1 = l - len(np.where(z[0, :] == "X")[0]) + len(np.where(z[0, :] == "X")[0]) * 2
    l1 = l1 - len(np.where(z[:, 0] == "X")[0]) + len(np.where(z[:, 0] == "X")[0]) * 2
    l2 = l - len(np.where(z[0, :] == "X")[0]) + len(np.where(z[0, :] == "X")[0]) * 1000000
    l2 = l2 - len(np.where(z[:, 0] == "X")[0]) + len(np.where(z[:, 0] == "X")[0]) * 1000000

    solution_1 += l1
    solution_2 += l2

# SOLUTIONS

print("Part One : " + str(solution_1) + "\nPart Two : " + str(solution_2))
