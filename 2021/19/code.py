# Advent of code Year 2021 Day 19 solution
# Author = brauni
# Date = 2021-12-21
"https://adventofcode.com/2021/day/19"

import re
from collections import Counter
import copy
import os
import math

solution_1, solution_2 = 0, 0

with open(os.getcwd() + "/2021/19/example.txt", 'r') as f:
    # with open(os.getcwd() + "/2021/19/input.txt", 'r') as f:
    input = f.read()
    input = input.split("\n\n")
    # input = []
    # for line in f.readlines():
    # input.append(int(line))
    # input = [int(line) for line in f.readlines()]
    # input = [line for line in f.readlines()]

# PART 0
scanners = []
for i in range(len(input)):
    scanners.append([])
    for line in input[i].split("\n"):
        scanners[i].append(int(line[-1]))


"""
print(input)
"""

# PART 1


# PART 2


# SOLUTIONS

print("Part One : " + str(solution_1) + "\nPart Two : " + str(solution_2))
