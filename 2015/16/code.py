# Advent of code Year 2015 Day 16 solution
# Author = brauni
# Date = 2023-12-06
"https://adventofcode.com/2015/day/16"

import re
from collections import Counter
import copy
import os
import math

solution_1, solution_2 = 0, 0

with open(os.getcwd() + "/AoC_private/2015/16/input.txt", "r") as f:
    # with open(os.getcwd() + "/2015/16/example.txt", 'r') as f:
    input = f.read()
    input = input.split("\n")
    # input = []
    # for line in f.readlines():
    # input.append(int(line))
    # input = [int(line) for line in f.readlines()]
    # input = [line for line in f.readlines()]

# PART 0

missing = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}

print(input)
sues = {}
for line in input:
    attributes = re.findall(r"\S+ \d+", line)
    sues[int(attributes[0].split()[1])] = {}
    for x in attributes[1:]:
        sues[int(attributes[0].split()[1])][x.split(": ")[0]] = int(x.split(": ")[1])

# PART 1
for sue in sues:
    for at in sues[sue]:
        if at in missing.keys():
            if missing[at] != sues[sue][at]:
                break
    else:
        solution_1 = sue

# PART 2
for sue in sues:
    for at in sues[sue]:
        if at in missing.keys() and at not in [
            "cats",
            "trees",
            "pomeranians",
            "goldfish",
        ]:
            if missing[at] != sues[sue][at]:
                break
        elif at in ["cats", "trees"]:
            if missing[at] >= sues[sue][at]:
                break
        elif at in ["pomeranians", "goldfish"]:
            if missing[at] <= sues[sue][at]:
                break
    else:
        solution_2 = sue

# SOLUTIONS

print("Part One : " + str(solution_1) + "\nPart Two : " + str(solution_2))
