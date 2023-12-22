# Advent of code Year 2023 Day 21 solution
# Author = brauni
# Date = 2023-12-21
"https://adventofcode.com/2023/day/21"

import re
from collections import Counter
import copy
import os
import math
import networkx as nx

solution_1, solution_2 = 0, 0

with open(os.getcwd() + "/AoC_private/2023/21/input.txt", "r") as f:
    # with open(os.getcwd() + "/2023/21/example.txt", "r") as f:
    input = f.read()
    input = input.split("\n")

print(input)


def bla(input, r):
    grid = set()
    starts = set()
    ttt = r // len(input) * 2 + 1
    sol = 0
    for i in range(ttt):
        for j in range(ttt):
            for n, line in enumerate(input):
                for m, c in enumerate(line):
                    if c != "#":
                        grid.add(complex(n + i * len(input), m + j * len(input[0])))
                        if c == "S":
                            starts.add(
                                complex(n + i * len(input), m + j * len(input[0]))
                            )
    s = sorted([x.real for x in starts if x.real == x.imag])[ttt // 2]
    start = [x for x in starts if x.real == s and x.imag == s][0]
    g2 = set()
    for x in grid:
        if abs(x.real - start.real) + abs(x.imag - start.imag) <= r:
            g2.add(x)
    G = nx.DiGraph()
    for x in g2:
        for dir in [1, 1j, -1, -1j]:
            if x + dir in g2:
                G.add_edge(x, x + dir)
    dist = nx.single_source_shortest_path_length(G, start, cutoff=r)
    for x in dist:
        if dist[x] % 2 == r % 2:
            sol += 1
    return sol


# PART 1
solution_1 = bla(input, 64)

# PART 2
goal_p2 = 26501365
a = bla(input, 65)
b = bla(input, 65 + len(input))
c = bla(input, 65 + len(input) * 2)
n = goal_p2 // len(input)
solution_2 = a + n * (b - a + (n - 1) * (c - b - b + a) // 2)
print("Part One : " + str(solution_1) + "\nPart Two : " + str(solution_2))
