# Advent of code Year 2015 Day 13 solution
# Author = brauni
# Date = 2023-11-17
"https://adventofcode.com/2015/day/13"

import re
from collections import Counter
import copy
import os
import math
import itertools


solution_1, solution_2 = 0, 0

# with open(os.getcwd() + "/2015/13/example.txt", "r") as f:
with open(os.getcwd() + "/2015/13/input.txt", "r") as f:
    input = f.read()
    input = input.split("\n")


# PART 0
print(input)

nodes = {}
for line in input:
    if line.split()[0] not in nodes.keys():
        nodes[line.split()[0]] = {}
    nodes[line.split()[0]][line.split()[10].replace(".", "")] = (
        int(line.split()[3]) if line.split()[2] == "gain" else -int(line.split()[3])
    )


# PART 1
name_combos = list(itertools.permutations(nodes.keys()))

for combo in name_combos:
    # print(combo)
    y = sum([nodes[combo[x]][combo[x + 1]] for x in range(len(combo) - 1)])
    y += nodes[combo[-1]][combo[0]]
    y += sum([nodes[combo[x]][combo[x - 1]] for x in range(len(combo) - 1, 0, -1)])
    y += nodes[combo[0]][combo[-1]]
    solution_1 = y if y > solution_1 else solution_1

combo = ["David", "Alice", "Bob", "Carol"]
[nodes[combo[x]][combo[x + 1]] for x in range(len(combo) - 1)]


# PART 2
nodes["myself"] = {}
for y in list(set([x.split()[0] for x in input])):
    nodes["myself"][y] = 0
    nodes[y]["myself"] = 0

name_combos = list(itertools.permutations(nodes.keys()))

for combo in name_combos:
    # print(combo)
    y = sum([nodes[combo[x]][combo[x + 1]] for x in range(len(combo) - 1)])
    y += nodes[combo[-1]][combo[0]]
    y += sum([nodes[combo[x]][combo[x - 1]] for x in range(len(combo) - 1, 0, -1)])
    y += nodes[combo[0]][combo[-1]]
    solution_2 = y if y > solution_2 else solution_2

# SOLUTIONS

print("Part One : " + str(solution_1) + "\nPart Two : " + str(solution_2))
