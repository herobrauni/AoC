# Advent of code Year 2015 Day 3 solution
# Author = brauni
# Date = 2023-11-17
"https://adventofcode.com/2015/day/3"

import re
from collections import Counter
import copy
import os
import math
import numpy as np

solution_1, solution_2 = 0, 0

# with open(os.getcwd() + "/2015/03/example.txt", "r") as f:
with open(os.getcwd() + "/AoC_private/2015/03/input.txt", "r") as f:
    input = f.read()
    # input = input.split("\n")
    # input = []
    # for line in f.readlines():
    # input.append(int(line))
    # input = [int(line) for line in f.readlines()]
    # input = [line for line in f.readlines()]

# PART 0


print(input)

grid = []
position = np.array([0, 0])
grid.append(tuple(position))
# print(position)
# PART 1
for x in input:
    if x == ">":
        position += np.array([0, 1])
    if x == "<":
        position += np.array([0, -1])
    if x == "^":
        position += np.array([1, 0])
    if x == "v":
        position += np.array([-1, 0])
    grid.append(tuple(position))

solution_1 = len(set(grid))
# print(set(grid))


# PART 2
grid = []
position_santa = np.array([0, 0])
position_robo = np.array([0, 0])
grid.append(tuple(position_santa))

count = 0
for x in input:
    if count % 2 == 0:
        position = position_santa
    elif count % 2 == 1:
        position = position_robo
    if x == ">":
        position += np.array([0, 1])
    if x == "<":
        position += np.array([0, -1])
    if x == "^":
        position += np.array([1, 0])
    if x == "v":
        position += np.array([-1, 0])
    grid.append(tuple(position))
    if count % 2 == 0:
        position_santa = position
    elif count % 2 == 1:
        position_robo = position
    count += 1

solution_2 = len(set(grid))


# SOLUTIONS

print("Part One : " + str(solution_1) + "\nPart Two : " + str(solution_2))
