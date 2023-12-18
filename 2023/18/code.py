# Advent of code Year 2023 Day 18 solution
# Author = brauni
# Date = 2023-12-18
"https://adventofcode.com/2023/day/18"

import re
from collections import Counter
import copy
import os
import math
import numpy as np

solution_1, solution_2 = 0, 0

with open(os.getcwd() + "/AoC_private/2023/18/input.txt", "r") as f:
    # with open(os.getcwd() + "/2023/18/example.txt", 'r') as f:
    input = f.read()
    input = input.split("\n")


# PART 0
def shoelace(dug):
    if type(dug) != list():
        dug = list(dug)
    sum = 0
    for i in range(len(dug)):
        n_1 = dug[i]
        n_2 = dug[(i + 1) % len(dug)]
        x_1, y_1 = n_1
        x_2, y_2 = n_2
        sum += x_1 * y_2 - y_1 * x_2
    area = abs(sum // 2)
    return area - len(dug) // 2 + 1 + len(dug)


# PART 1
dug_p1 = set()
x, y = 0, 0
for line in input:
    direction, length, color = line.split()
    match direction:
        case "R":
            dx = 0
            dy = 1
        case "L":
            dx = 0
            dy = -1
        case "D":
            dx = 1
            dy = 0
        case "U":
            dx = -1
            dy = 0
    dug_p1.add((x, y))
    for i in range(int(length)):
        x = x + dx
        y = y + dy
        dug_p1.add((x, y))

solution_1 = shoelace(dug_p1)

# PART 2
dug_p2 = set()
x, y = 0, 0
for line in input:
    direction, length, color = line.split()
    color = re.findall(r"[\d|[a-f]+", color)[0]
    direction = color[-1]
    length = int(color[:-1], 16)
    match direction:
        case "0":
            dx = 0
            dy = 1
        case "1":
            dx = 1
            dy = 0
        case "2":
            dx = 0
            dy = -1
        case "3":
            dx = -1
            dy = 0
    dug_p2.add((x, y))
    for i in range(int(length)):
        x = x + dx
        y = y + dy
        dug_p2.add((x, y))

solution_2 = shoelace(dug_p2)

# SOLUTIONS

print("Part One : " + str(solution_1) + "\nPart Two : " + str(solution_2))
