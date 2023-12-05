# Advent of code Year 2015 Day 9 solution
# Author = brauni
# Date = 2023-11-17
"https://adventofcode.com/2015/day/9"

import re
from collections import Counter
import copy
import os
import math
import networkx as nx
import itertools

solution_1, solution_2 = 0, 0

# with open(os.getcwd() + "/2015/09/example.txt", "r") as f:
with open(os.getcwd() + "/AoC_private/2015/09/input.txt", "r") as f:
    input = f.read()
    input = input.split("\n")
    # input = []
    # for line in f.readlines():
    # input.append(int(line))
    # input = [int(line) for line in f.readlines()]
    # input = [line for line in f.readlines()]

# PART 0


print(input)


nodes = {}
for line in input:
    if line.split()[0] not in nodes.keys():
        nodes[line.split()[0]] = {}
    nodes[line.split()[0]][line.split()[2]] = int(line.split()[4])
    if line.split()[2] not in nodes.keys():
        nodes[line.split()[2]] = {}
    nodes[line.split()[2]][line.split()[0]] = int(line.split()[4])


bla = list(itertools.permutations(nodes.keys()))
solution_1 = 99999999999

# PART 1
for directions in bla:
    y = sum(
        [nodes[directions[x]][directions[x + 1]] for x in range(len(directions) - 1)]
    )
    solution_1 = y if y < solution_1 else solution_1
# PART 2
solution_2 = 0
for directions in bla:
    y = sum(
        [nodes[directions[x]][directions[x + 1]] for x in range(len(directions) - 1)]
    )
    solution_2 = y if y > solution_2 else solution_2
# SOLUTIONS

print("Part One : " + str(solution_1) + "\nPart Two : " + str(solution_2))
