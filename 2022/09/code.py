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
with open(os.getcwd() + "/2022/09/input.txt", 'r') as f:
    input = f.read()
    input = input.split("\n")
    # input = []
    # for line in f.readlines():
    # input.append(int(line))
    # input = [int(line) for line in f.readlines()]
    # input = [line for line in f.readlines()]

# PART 0


print(input)


def move_tail(h, t):
    if round(np.linalg.norm(h-t)) > 1:
        if h[0] == t[0]:  # same x
            t[1] = t[1] + 1 if h[1] > t[1] else t[1]-1
        elif h[1] == t[1]:  # same y
            t[0] = t[0] + 1 if h[0] > t[0] else t[0]-1
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


def move_head(h, direction):
    right = np.array([1, 0])
    left = np.array([-1, 0])
    up = np.array([0, 1])
    down = np.array([0, -1])
    match direction:
        case "U": h = np.add(h, up)
        case "D": h = np.add(h, down)
        case "L": h = np.add(h, left)
        case "R": h = np.add(h, right)
    return h


# PART 1
h = np.array([0, 0])
t = np.array([0, 0])
visited = []


for line in input:
    direction = line.split()[0]
    distance = int(line.split()[1])
    for i in range(distance):
        h = move_head(h, direction)
        t = move_tail(h, t)
        visited.append(tuple(t))
solution_1 = len(set(visited))

# PART 2
h = np.array([0, 0])
t = np.array([0, 0])
visited = []
tails = [np.array([0, 0]) for x in range(9)]

for line in input:
    direction = line.split()[0]
    distance = int(line.split()[1])
    for i in range(distance):
        h = move_head(h, direction)
        tails[0] = move_tail(h, tails[0])
        for x in range(8):
            tails[x+1] = move_tail(tails[x], tails[x+1])
        visited.append(tuple(tails[8]))
solution_2 = len(set(visited))

# SOLUTIONS

print("Part One : " + str(solution_1) + "\nPart Two : " + str(solution_2))
