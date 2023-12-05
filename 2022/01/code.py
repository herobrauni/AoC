# Advent of code Year 2022 Day 1 solution
# Author = brauni
# Date = 2022-12-01
"https://adventofcode.com/2022/day/1"

import re
from collections import Counter
import copy
import os
import math

solution_1, solution_2 = 0, 0


# with open(os.getcwd() + "/2022/01/example.txt", 'r') as f:
with open(os.getcwd() + "/AoC_private/2022/01/input.txt", "r") as f:
    input = f.read()
    input = input.split("\n\n")
    # input = []
    # for line in f.readlines():
    # input.append(int(line))
    # input = [int(line) for line in f.readlines()]
    # input = [line for line in f.readlines()]

# PART 0

# print(input)

# PART 1
for x in input:
    y = sum([int(z) for z in x.split("\n")])
    if y > solution_1:
        solution_1 = y

# PART 2
ranking = []
for x in input:
    y = sum([int(z) for z in x.split("\n")])
    ranking.append(y)
ranking.sort()
ranking.reverse()
# print(ranking)
solution_2 = sum(ranking[:3])

# SOLUTIONS


print("Part One : " + str(solution_1) + "\nPart Two : " + str(solution_2))
