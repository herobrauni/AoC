# Advent of code Year 2022 Day 14 solution
# Author = brauni
# Date = 2022-12-14
"https://adventofcode.com/2022/day/14"

import re
from collections import Counter
import copy
import os
import math
import numpy as np

solution_1, solution_2 = 0, 0

# with open(os.getcwd() + "/2022/14/example.txt", 'r') as f:
with open(os.getcwd() + "/AoC_private/2022/14/input.txt", "r") as f:
    input = f.read()
    input = input.split("\n")
    # input = []
    # for line in f.readlines():
    # input.append(int(line))
    # input = [int(line) for line in f.readlines()]
    # input = [line for line in f.readlines()]

# PART 0


print(input)
for i in range(len(input)):
    input[i] = input[i].split(" -> ")
    input[i] = [eval(x) for x in input[i]]

for line in input:
    print(line)

# find min/max
min_x, max_x, min_y, max_y = 100000, 0, 100000, 0
for i in range(len(input)):
    for j in range(len(input[i])):
        min_x = input[i][j][0] if input[i][j][0] < min_x else min_x
        min_y = input[i][j][1] if input[i][j][1] < min_y else min_y
        max_x = input[i][j][0] if input[i][j][0] > max_x else max_x
        max_y = input[i][j][1] if input[i][j][1] > max_y else max_y


def fall(x, y, grid):
    sandx, sandy = x, y
    if sandy + 1 < len(grid):
        if grid[sandy + 1, sandx] == 0:
            # sandy = sandy + 1
            return fall(sandx, sandy + 1, grid)
        elif sandx - 1 >= 0:
            if grid[sandy + 1, sandx - 1] == 0:
                return fall(sandx - 1, sandy + 1, grid)
                # sandy = sandy + 1
                # sandx = sandx - 1
            elif sandx + 1 < len(grid[0]):
                if grid[sandy + 1, sandx + 1] == 0:
                    return fall(sandx + 1, sandy + 1, grid)
                    # sandy = sandy + 1
                    # sandx = sandx + 1
            else:
                return False
        else:
            return False
    else:
        return False
    grid[sandy, sandx] = 8
    return grid


# PART 1
grid = np.zeros(((max_x - min_x + 1) * (max_y + 1),), dtype=int).reshape(
    max_y + 1, (max_x - min_x + 1)
)

for i in range(len(input)):
    prex, prey = input[i][0][0], input[i][0][1]
    grid[prey, prex - min_x] = "1"
    for j in range(1, len(input[i])):
        # print(grid)
        x, y = input[i][j][0], input[i][j][1]
        while x != prex:
            # print(grid)
            grid[y, x - min_x] = "1"
            x = x - 1 if x > prex else x + 1
        while y != prey:
            # print(grid)
            grid[y, x - min_x] = "1"
            y = y - 1 if y > prey else y + 1
        prex, prey = input[i][j][0], input[i][j][1]

while True:
    x = fall(500 - min_x, 0, grid)
    if x is not False:
        grid = x
        solution_1 += 1
    else:
        break

# # PART 2
scale = (max_y + 2 + 1) * 2
# 289
grid = np.zeros(((max_x - min_x + 1 + scale) * (max_y + 2 + 1),), dtype=int).reshape(
    max_y + 2 + 1, (max_x - min_x + 1 + scale)
)

s = scale // 2 - 1
for i in range(len(input)):
    prex, prey = input[i][0][0] + s, input[i][0][1]
    grid[prey, prex - min_x] = "1"
    for j in range(1, len(input[i])):
        # print(grid)
        x, y = input[i][j][0] + s, input[i][j][1]
        while x != prex:
            # print(grid)
            grid[y, x - min_x] = "1"
            x = x - 1 if x > prex else x + 1
        while y != prey:
            # print(grid)
            grid[y, x - min_x] = "1"
            y = y - 1 if y > prey else y + 1
        prex, prey = input[i][j][0] + s, input[i][j][1]

for i in range(len(grid[0])):
    grid[len(grid) - 1][i] = 1
# print(grid)

while True:
    # print(solution_2)
    x = fall(500 - min_x + s, 0, grid)
    if x is not False:
        grid = x
        solution_2 += 1
    else:
        break
    if grid[0, 500 - min_x + s] == 8:
        break

print("Part One : " + str(solution_1) + "\nPart Two : " + str(solution_2))
