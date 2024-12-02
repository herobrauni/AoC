# Advent of code Year 2021 Day 5 solution
# Author = brauni
# Date = 2021-12-05
import re
from collections import Counter
import copy
import os

solution_1, solution_2 = 0, 0
# with open(os.getcwd() + "\\2021\\05\\example.txt", 'r') as f:
with open(os.getcwd() + "\\2021\\05\\input.txt", "r") as f:
    input = f.read()
    input = input.split("\n")
    input = [re.split(" -> |,", x) for x in input]
    # input = [x.split(",") for x in [y for y in input]]
    # input = []
    # for line in f.readlines():
    # input.append(int(line))
    # input = [int(line) for line in f.readlines()]
    # input = [line for line in f.readlines()]

"""
print(input)
"""

# PART 1
t0 = []
for line in input:
    for row in line:
        t0.append(int(row))

t1 = []
for i in range(0, len(t0), 4):
    t1.append([x for x in t0[i : i + 4]])

diagram = [[0] * (max(map(max, t1)) + 1) for i in range((max(map(max, t1))) + 1)]

for line in t1:
    # print(abs(line[0] - line[2]), abs(line[1] - line[3]))
    if line[1] == line[3]:  # horizontal
        for i in range(abs(line[0] - line[2]) + 1):
            if line[0] < line[2]:  # left to right
                diagram[line[1]][line[0] + i] += 1
            if line[0] > line[2]:  # right to left
                diagram[line[1]][line[0] - i] += 1
    elif line[0] == line[2]:  # vertical
        for i in range(abs(line[1] - line[3]) + 1):
            if line[1] < line[3]:  # top to bottom
                diagram[line[1] + i][line[0]] += 1
            if line[1] > line[3]:  # bottom to top
                diagram[line[1] - i][line[0]] += 1


for line in diagram:
    for row in line:
        if row > 1:
            solution_1 += 1

# PART 2

for line in t1:
    # diagonal bottom right to top left
    if line[0] > line[2] and line[1] > line[3]:
        for i in range(abs(line[0] - line[2]) + 1):
            diagram[line[1] - i][line[0] - i] += 1
    # diagonal top left to bottom right
    elif line[0] < line[2] and line[1] < line[3]:
        for i in range(abs(line[0] - line[2]) + 1):
            diagram[line[1] + i][line[0] + i] += 1
    # diagonal bottom left to top right
    elif line[0] < line[2] and line[1] > line[3]:
        for i in range(abs(line[0] - line[2]) + 1):
            diagram[line[1] - i][line[0] + i] += 1
    # diagonal top right to bottom left
    elif line[0] > line[2] and line[1] < line[3]:
        for i in range(abs(line[0] - line[2]) + 1):
            diagram[line[1] + i][line[0] - i] += 1


for line in diagram:
    for row in line:
        if row > 1:
            solution_2 += 1

# for line in diagram:
#     print(line)

# SOLUTIONS

print("Part One : " + str(solution_1) + "\nPart Two : " + str(solution_2))
