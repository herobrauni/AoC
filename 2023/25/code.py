# Advent of code Year 2023 Day 25 solution
# Author = brauni
# Date = 2023-12-26
"https://adventofcode.com/2023/day/25"

import re
from collections import Counter
import copy
import os
import math
import networkx as nx

solution_1, solution_2 = 0, 0

with open(os.getcwd() + "/AoC_private/2023/25/input.txt", "r") as f:
    # with open(os.getcwd() + "/2023/25/example.txt", "r") as f:
    input = f.read()
    input = input.split("\n")

# PART 0
print(input)


# PART 1
G = nx.Graph()
bla = {}
for line in input:
    x, y = line.split(": ")
    y = y.split(" ")
    bla[x] = y
    G.add_node(x)
    for yy in y:
        G.add_node(yy)
        G.add_edge(x, yy)


# Thanks https://beta.devtoolsdaily.com/graphviz
G.remove_edge("kfr", "vkp")
G.remove_edge("rhk", "bff")
G.remove_edge("qpp", "vnm")


start = "qbx"
set1 = set()
set2 = set()
for x in G.nodes():
    if nx.has_path(G, start, x):
        set1.add(x)
    else:
        set2.add(x)

solution_1 = len(set1) * len(set2)

# SOLUTIONS
print("Part One : " + str(solution_1) + "\nPart Two : " + str(solution_2))
