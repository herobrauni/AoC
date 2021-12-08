# Advent of code Year 2021 Day 7 solution
# Author = brauni
# Date = 2021-12-07
"https://adventofcode.com/2021/day/7"

# Does not work for p2 if the best position is not a starting position of a crab

import re
from collections import Counter
import copy
import os

solution_1, solution_2 = 0, 0

with open(os.getcwd() + "\\2021\\07\\example.txt", 'r') as f:
    # with open(os.getcwd() + "\\2021\\07\\input.txt", 'r') as f:
    input = f.read()
    input = [int(line) for line in input.split(",")]
    # input = []
    # for line in f.readlines():
    # input.append(int(line))
    # input = [int(line) for line in f.readlines()]
    # input = [line for line in f.readlines()]

# PART 0

"""
print(input)
"""

# PART 1
fuel = []
for i in range(len(input)):
    f = 0
    for j in range(len(input)):
        f += (abs(input[i]-input[j]))
    fuel.append(f)

solution_1 = min(fuel)


# PART 2
fuel = []
for i in range(len(input)):
    f = 0
    for j in range(len(input)):
        # 1/2 n (1 + n)
        f += (1/2)*(abs(input[i]-input[j]))*(1 + abs(input[i]-input[j]))
    fuel.append(f)

solution_2 = int(min(fuel))


# SOLUTIONS

print("Part One : " + str(solution_1) + "\nPart Two : " + str(solution_2))
