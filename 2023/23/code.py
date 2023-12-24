# Advent of code Year 2023 Day 23 solution
# Author = brauni
# Date = 2023-12-24
"https://adventofcode.com/2023/day/23"

import re
from collections import Counter
import copy
import os
import math
import networkx as nx

solution_1, solution_2 = 0, 0

with open(os.getcwd() + "/AoC_private/2023/23/input.txt", 'r') as f:
# with open(os.getcwd() + "/2023/23/example.txt", "r") as f:
    input = f.read()
    input = input.split("\n")
    # input = []
    # for line in f.readlines():
    # input.append(int(line))
    # input = [int(line) for line in f.readlines()]
    # input = [line for line in f.readlines()]

# PART 0


print(input)


def bla(input, p=1):
    grid = set()
    grid_slopes = {}
    sol = 0
    for n, line in enumerate(input):
        for m, c in enumerate(line):
            if c == ".":
                grid.add(complex(n, m))
            elif c in "<>v^":
                grid_slopes[complex(n, m)] = c
    start = [x for x in grid if x.real == 0][0]
    end = [x for x in grid if x.real == len(input) - 1][0]
    G = nx.DiGraph()
    if p == 2:
        for x in grid_slopes:
            grid.add(x)
    for x in grid:
        for dir in [1, 1j, -1, -1j]:
            if x + dir in grid:
                G.add_edge(x, x + dir)
    if p == 1:
        for x in grid_slopes:
            if grid_slopes[x] == ">":
                G.add_edge(x - 1j, x)
                G.add_edge(x, x + 1j)
            elif grid_slopes[x] == "<":
                G.add_edge(x + 1j, x)
                G.add_edge(x, x - 1j)
            elif grid_slopes[x] == "v":
                G.add_edge(x - 1, x)
                G.add_edge(x, x + 1)
            elif grid_slopes[x] == "^":
                G.add_edge(x + 1, x)
                G.add_edge(x, x - 1)
    paths = nx.all_simple_paths(G, start, end)
    return paths


# PART 1
# grid, grid_slopes = bla(input)
paths = bla(input, 1)
solution_1 = max([len(x) for x in paths]) - 1

paths2 = bla(input, 2)
solution_2 = max([len(x) for x in paths2]) - 1

# PART 2


# SOLUTIONS

print("Part One : " + str(solution_1) + "\nPart Two : " + str(solution_2))
