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
with open(os.getcwd() + "\\2021\\12\\input.txt", "r") as f:
    input = f.read()
    input = input.split("\n")

# PART 0
# Split the inputs into connections A <-> B
# sort them so that A can not be "end" and B can not be "start"
input = [line.split("-") for line in input]
for i in range(len(input)):
    if input[i][0] == "end":
        # print(input[i])
        input[i][0], input[i][1] = input[i][1], input[i][0]
    if input[i][1] == "start":
        input[i][0], input[i][1] = input[i][1], input[i][0]

# Create a dictonary of all connections/destinations of a single point (i.e. A: "c,d,e" )
# "start" can not be in destinations and "end" can not be a key in the dictonary
paths = {}
for line in input:
    if line[0] not in paths:
        paths[line[0]] = []
    if line[1] != "start":
        paths[line[0]].append(line[1])
for line in input:
    if line[1] not in paths and line[1] != "end":
        paths[line[1]] = []
    if line[0] != "start" and line[1] != "end":
        paths[line[1]].append(line[0])

"""
print(input)
"""
# PART 1

all_paths = []


def get_path(start, path, p2: bool = False):
    global all_paths
    if start == "end":
        return path + ["end"]
    if start not in paths:
        return None
    for i in paths[start]:
        if i not in path or i.isupper():
            new_path = get_path(i, path + [start], p2)
            if new_path:
                all_paths.append(new_path)
        elif p2:
            test = path + [start]
            if len([x for x in test if test.count(x) > 1 and x.islower()]) < 2:
                new_path = get_path(i, path + [start], p2)


get_path("start", [])
solution_1 = len(all_paths)
all_paths = []
get_path("start", [], p2=True)
solution_2 = len(all_paths)


# SOLUTIONS
print("Part One : " + str(solution_1) + "\nPart Two : " + str(solution_2))
