# Advent of code Year 2023 Day 10 solution
# Author = brauni
# Date = 2023-12-10
"https://adventofcode.com/2023/day/10"

import re
from collections import Counter
import copy
import os
import math
import numpy as np

solution_1, solution_2 = 0, 0

with open(os.getcwd() + "/AoC_private/2023/10/input.txt", "r") as f:
    # with open(os.getcwd() + "/2023/10/example.txt", "r") as f:
    input = f.read()
    input = input.split("\n")

# PART 0
# print(input)
grid = np.array([t for t in "".join([x for x in input])])
# len(input[0])
# len(input)
grid = grid.reshape(len(input), len(input[0]))
grid = np.pad(grid, pad_width=1, constant_values=",")

# PART 1
s = np.where(grid == "S")
start = (s[0][0], s[1][0])

current = "X"
for direction in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
    if grid[start[0] + direction[0], start[1] + direction[1]] in [
        "J",
        "-",
        "7",
    ] and direction == (0, 1):
        p = (start[0] + direction[0], start[1] + direction[1])
        break
    elif grid[start[0] + direction[0], start[1] + direction[1]] in [
        "|",
        "J",
        "L",
    ] and direction == (1, 0):
        p = (start[0] + direction[0], start[1] + direction[1])
        break
    elif grid[start[0] + direction[0], start[1] + direction[1]] in [
        "-",
        "F",
        "L",
    ] and direction == (0, -1):
        p = (start[0] + direction[0], start[1] + direction[1])
        break
    elif grid[start[0] + direction[0], start[1] + direction[1]] in [
        "|",
        "F",
        "7",
    ] and direction == (-1, 0):
        p = (start[0] + direction[0], start[1] + direction[1])
        break

g2 = np.full((len(grid) * 2, len(grid[0]) * 2), ",")
g2[(start[0] * 2 + 1, start[1] * 2)] = "S"
path = []
path.append(start)

while p not in path:
    path.append(p)
    g2[(p[0] * 2, p[1] * 2)] = grid[p]
    match grid[p]:
        case "|":
            x = (p[0] + 1, p[1])
            y = (p[0] - 1, p[1])
        case "-":
            x = (p[0], p[1] + 1)
            y = (p[0], p[1] - 1)
        case "L":
            x = (p[0] - 1, p[1])
            y = (p[0], p[1] + 1)
        case "J":
            x = (p[0] - 1, p[1])
            y = (p[0], p[1] - 1)
        case "7":
            x = (p[0] + 1, p[1])
            y = (p[0], p[1] - 1)
        case "F":
            x = (p[0] + 1, p[1])
            y = (p[0], p[1] + 1)
        case _:
            print("Error", p, grid[p])
            break
    p = x if x not in path else y


# solution_1 = round(length / 2)

# # # PART 2
g2 = np.full((len(grid) * 2, len(grid[0]) * 2), ",")
for p in path:
    g2[(p[0] * 2, p[1] * 2)] = grid[p]
    match grid[p]:
        case "|":
            x = (p[0] * 2 + 1, p[1] * 2)
            y = (p[0] * 2 - 1, p[1] * 2)
        case "-":
            x = (p[0] * 2, p[1] * 2 + 1)
            y = (p[0] * 2, p[1] * 2 - 1)
        case "L":
            x = (p[0] * 2 - 1, p[1] * 2)
            y = (p[0] * 2, p[1] * 2 + 1)
        case "J":
            x = (p[0] * 2 - 1, p[1] * 2)
            y = (p[0] * 2, p[1] * 2 - 1)
        case "7":
            x = (p[0] * 2 + 1, p[1] * 2)
            y = (p[0] * 2, p[1] * 2 - 1)
        case "F":
            x = (p[0] * 2 + 1, p[1] * 2)
            y = (p[0] * 2, p[1] * 2 + 1)
        case "S":
            continue
    g2[x] = "X"
    g2[y] = "X"

asdjh = list(np.ndindex(*g2.shape))
for b in [x for x in asdjh if x[0] in [0, len(g2) - 1] or x[1] in [0, len(g2[0]) - 1]]:
    g2[b] = "."
change = True
while change:
    # for i in range(1):
    change = False
    for a in [x for x in asdjh if g2[x] == ","]:
        for direction in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            if g2[(a[0] + direction[0], a[1] + direction[1])] == ".":
                g2[a] = "."
                change = True
                break

# for line in g2:
#     print("".join([str(x) for x in line]))


test = list(np.ndindex(*grid.shape))
for g in test:
    grid[g] = g2[(g[0] * 2, g[1] * 2)]

# for line in grid:
#     print("".join([str(x) for x in line]))

solution_1 = round(len(path) / 2)
solution_2 = (grid == ",").sum()

# SOLUTIONS

print("Part One : " + str(solution_1) + "\nPart Two : " + str(solution_2))
