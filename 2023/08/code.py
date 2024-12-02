# Advent of code Year 2023 Day 8 solution
# Author = brauni
# Date = 2023-12-08
"https://adventofcode.com/2023/day/8"

import re
from collections import Counter
import copy
import os
import math

solution_1, solution_2 = 0, 0

with open(os.getcwd() + "/AoC_private/2023/08/input.txt", "r") as f:
    # with open(os.getcwd() + "/2023/08/example.txt", "r") as f:
    input = f.read()
    input = input.split("\n")
    # input = []
    # for line in f.readlines():
    # input.append(int(line))
    # input = [int(line) for line in f.readlines()]
    # input = [line for line in f.readlines()]

# PART 0


print(input)
instructions = input[0]
directions = {}
for x in input[2:]:
    z = re.findall(r"[A-Z]+", x)
    directions[z[0]] = z[1:]

# PART 1
location = "AAA"
c = 0
while location != "ZZZ":
    if instructions[c] == "L":
        location = directions[location][0]
    elif instructions[c] == "R":
        location = directions[location][1]
    c += 1
    solution_1 += 1
    if c >= len(instructions):
        c = 0


# PART 2
locations = [x for x in list(directions.keys()) if re.search(r"[A-Z]{2}A", x)]
hits = []
for location in locations:
    c = 0
    z = 0
    while not re.match(r"[A-Z]{2}Z", location):
        if instructions[c] == "L":
            location = directions[location][0]
        elif instructions[c] == "R":
            location = directions[location][1]
        c += 1
        z += 1
        if c >= len(instructions):
            c = 0
    hits.append(z)
solution_2 = math.lcm(*hits)
# SOLUTIONS

print("Part One : " + str(solution_1) + "\nPart Two : " + str(solution_2))
