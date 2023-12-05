# Advent of code Year 2015 Day 2 solution
# Author = brauni
# Date = 2023-11-17
"https://adventofcode.com/2015/day/2"

import re
from collections import Counter
import copy
import os
import math

solution_1, solution_2 = 0, 0

# with open(os.getcwd() + "/2015/02/example.txt", "r") as f:
with open(os.getcwd() + "/AoC_private/2015/02/input.txt", "r") as f:
    input = f.read()
    input = input.split("\n")
    input = [x.split("x") for x in input]
    # input = []
    # for line in f.readlines():
    # input.append(int(line))
    # input = [int(line) for line in f.readlines()]
    # input = [line for line in f.readlines()]

# PART 0
print(input)

# PART 1
for c in input:
    lw = int(c[0]) * int(c[1])
    wh = int(c[1]) * int(c[2])
    hl = int(c[2]) * int(c[0])
    x = 2 * lw + 2 * wh + 2 * hl
    x += min(lw, wh, hl)
    solution_1 += x

# PART 2
for c in input:
    bow = math.prod([int(x) for x in c])
    ribbon = sorted([int(x) for x in c])[0] * 2 + sorted([int(x) for x in c])[1] * 2
    solution_2 += bow + ribbon

# SOLUTIONS
print("Part One : " + str(solution_1) + "\nPart Two : " + str(solution_2))
