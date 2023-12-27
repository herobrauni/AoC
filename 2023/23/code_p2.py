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
grid = set()
for n, line in enumerate(input):
    for m, c in enumerate(line):
        if c != "#":
            grid.add(complex(n, m))

start = 0 + 1j
end = complex(len(input) - 1, len(input[0]) - 2)

G = nx.Graph()
G.add_nodes_from(grid)
for x in grid:
    for dir in [1, 1j, -1, -1j]:
        if x + dir in grid:
            G.add_edge(x, x + dir, weight=1)


len(G.nodes)
for x in list(G.nodes):
    nxt = list(G.neighbors(x))
    if len(nxt) == 2:
        G.add_edge(
            nxt[0], nxt[1], weight=sum(G.get_edge_data(a, x)["weight"] for a in nxt)
        )
        G.remove_node(x)
    if len(nxt) == 0:
        G.remove_node(x)
    if len(nxt) == 1 and x != start and x != end:
        G.remove_node(x)
len(G.nodes)

pppp = nx.all_simple_paths(G, start, end)

for x in pppp:
    z = nx.path_weight(G, x, weight="weight")
    if z > solution_2:
        solution_2 = z
        # print(z, x, len(x))
# SOLUTIONS


print("Part One : " + str(solution_1) + "\nPart Two : " + str(solution_2))
