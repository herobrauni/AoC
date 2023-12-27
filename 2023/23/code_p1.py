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

with open(os.getcwd() + "/AoC_private/2023/23/input.txt", "r") as f:
    # with open(os.getcwd() + "/2023/23/example.txt", "r") as f:
    input = f.read()
    input = input.split("\n")

# PART 0
print(input)


def bla(input, start, end):
    grid = set()
    grid_slopes = {}
    for n, line in enumerate(input):
        for m, c in enumerate(line):
            if c == ".":
                grid.add(complex(n, m))
            elif c in "<>v^":
                grid_slopes[complex(n, m)] = c
    G = nx.DiGraph()
    for x in grid:
        for dir in [1, 1j, -1, -1j]:
            if x + dir in grid:
                G.add_edge(x, x + dir)
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
    return paths, grid_slopes


# PART 1
# grid, grid_slopes = bla(input)
paths, grid_slopes = bla(input, 0 + 1j, complex(len(input) - 1, len(input[0]) - 2))
solution_1 = max([len(x) for x in paths]) - 1

# SOLUTIONS

print("Part One : " + str(solution_1) + "\nPart Two : " + str(solution_2))
