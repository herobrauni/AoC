# Advent of code Year 2022 Day 9 solution
# Author = brauni
# Date = 2022-12-09
"https://adventofcode.com/2022/day/9"

import re
from collections import Counter
import copy
import os
import math
import numpy as np

solution_1, solution_2 = 0, 0

# with open(os.getcwd() + "/2022/09/example.txt", 'r') as f:
with open(os.getcwd() + "/AoC_private/2022/09/input.txt", "r") as f:
    input = f.read()
    input = input.split("\n")
    # input = []
    # for line in f.readlines():
    # input.append(int(line))
    # input = [int(line) for line in f.readlines()]
    # input = [line for line in f.readlines()]

# PART 0


print(input)

grid = []
b = 1000
x, y = 500, 500
for i in range(b):
    grid.append([0] * b)
s = np.array([x, y])
h = np.array([x, y])
t = np.array([x, y])
grid[x, y] = 1
# PART 1


def move(h, t):
    if round(np.linalg.norm(h - t)) > 1:
        if h[0] == t[0]:  # same x
            t[1] = t[1] + 1 if h[1] > t[1] else t[1] - 1
        elif h[1] == t[1]:  # same y
            t[0] = t[0] + 1 if h[0] > t[0] else t[0] - 1
        else:
            if h[0] > t[0] and h[1] > t[1]:  # up and right
                t = np.add(t, [1, 1])
            elif h[0] > t[0] and h[1] < t[1]:  # up and left
                t = np.add(t, [1, -1])
            elif h[0] < t[0] and h[1] < t[1]:  # down and left
                t = np.add(t, [-1, -1])
            elif h[0] < t[0] and h[1] > t[1]:  # down and right
                t = np.add(t, [-1, 1])
        # print(t)
    return t


for line in input:
    direction = line.split()[0]
    distance = int(line.split()[1])
    for i in range(0, int(distance)):
        match direction:
            case "R":
                j = np.array([1, 0])
            case "L":
                j = np.array([-1, 0])
            case "U":
                j = np.array([0, 1])
            case "D":
                j = np.array([0, -1])
        h = np.add(h, j)
        t = move(h, t)
        grid[t[0]][t[1]] = 1
        # print(h, t)
solution_1 = sum([sum(l) for l in grid])
# PART 2

grid = []
b = 1000
x, y = 500, 500
for i in range(b):
    grid.append([0] * b)
s = np.array([x, y])
h = np.array([x, y])
t1, t2, t3, t4, t5, t6, t7, t8, t9 = (
    np.array([x, y]),
    np.array([x, y]),
    np.array([x, y]),
    np.array([x, y]),
    np.array([x, y]),
    np.array([x, y]),
    np.array([x, y]),
    np.array([x, y]),
    np.array([x, y]),
)
grid[x, y] = 1

for line in input:
    direction = line.split()[0]
    distance = int(line.split()[1])
    for i in range(0, int(distance)):
        match direction:
            case "R":
                j = np.array([1, 0])
            case "L":
                j = np.array([-1, 0])
            case "U":
                j = np.array([0, 1])
            case "D":
                j = np.array([0, -1])
        h = np.add(h, j)
        t1 = move(h, t1)
        t2 = move(t1, t2)
        t3 = move(t2, t3)
        t4 = move(t3, t4)
        t5 = move(t4, t5)
        t6 = move(t5, t6)
        t7 = move(t6, t7)
        t8 = move(t7, t8)
        t9 = move(t8, t9)
        grid[t9[0]][t9[1]] = 1
solution_2 = sum([sum(l) for l in grid])

# SOLUTIONS


print("Part One : " + str(solution_1) + "\nPart Two : " + str(solution_2))
