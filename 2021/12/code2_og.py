# Advent of code Year 2021 Day 12 solution
# Author = brauni
# Date = 2021-12-12
"https://adventofcode.com/2021/day/12"

import re
from collections import Counter
import copy
import os
import math

solution_1, solution_2 = 0, 0

# with open(os.getcwd() + "\\2021\\12\\example.txt", 'r') as f:
with open(os.getcwd() + "\\2021\\12\\input.txt", 'r') as f:
    input = f.read()
    input = input.split("\n")
    # input = []
    # for line in f.readlines():
    # input.append(int(line))
    # input = [int(line) for line in f.readlines()]
    # input = [line for line in f.readlines()]

# PART 0
input2 = [line.split("-") for line in input]
"""
print(input2)
"""


# input3 = list(dict.fromkeys(input3))


# PART 1
paths = {}
for line in input2:
    if line[0] not in paths:
        paths[line[0]] = []
    paths[line[0]].append(line[1])
for line in input2:
    if line[1] not in paths:  # and line[1] != "end" and line[1] != "start":
        paths[line[1]] = []
    paths[line[1]].append(line[0])


lines = []
for starts in paths["start"]:
    lines.append(["start", starts])


for y in range(30):
    for i in range(len(lines)):
        if lines[i][-1] == "end":
            continue
        double_visit_possible = True
        visited = [x for x in lines[i] if x.islower()]
        if len([x for x in visited if visited.count(x) > 1]) > 0:
            double_visit_possible = False
        for j in paths[lines[i][-1]]:
            if j == "start":
                continue
            if lines[i] + [j] not in lines:  # lines[i][-1] != "start" and
                if double_visit_possible:
                    lines.append(lines[i] + [j])
                elif j not in visited:
                    lines.append(lines[i] + [j])
    path_no_duplicates = []
    for line in lines:
        if line[-1] == "end" and line not in path_no_duplicates:
            path_no_duplicates.append(line)
    print(y, len(path_no_duplicates))


path_no_duplicates = []
for line in lines:
    if line[-1] == "end" and line not in path_no_duplicates:
        path_no_duplicates.append(line)
solution_1 = len(path_no_duplicates)
# PART 2


# for line in path_no_duplicates:
#     print(line)
# SOLUTIONS


print("Part One : " + str(solution_1) + "\nPart Two : " + str(solution_2))
