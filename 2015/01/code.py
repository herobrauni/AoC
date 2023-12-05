# Advent of code Year 2015 Day 1 solution
# Author = brauni
# Date = 2023-11-17
"https://adventofcode.com/2015/day/1"

import re
from collections import Counter
import copy
import os
import math

solution_1, solution_2 = 0, 0

# with open(os.getcwd() + "/2015/01/example.txt", 'r') as f:
with open(os.getcwd() + "/AoC_private/2015/01/input.txt", "r") as f:
    input = f.read()
    # input = input.split("\n")
    # input = []
    # for line in f.readlines():
    # input.append(int(line))
    # input = [int(line) for line in f.readlines()]
    # input = [line for line in f.readlines()]

# PART 0


print(input)


# PART 1
solution_1 = 0

solution_1 += input.count("(")
solution_1 -= input.count(")")

print(solution_1)

# PART 2
solution_2 = 0
floor = 0
for c in input:
    solution_2 += 1
    if c == "(":
        floor += 1
    if c == ")":
        floor -= 1
    if floor == -1:
        break

# SOLUTIONS

print("Part One : " + str(solution_1) + "\nPart Two : " + str(solution_2))
