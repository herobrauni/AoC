# Advent of Code Year 2025 Day 11 solution
# Author = brauni
# Date = 2025-12-11

import os

import networkx as nx
from aocd import submit
from aocd.models import Puzzle

puzzle = Puzzle(year=2025, day=11)


# with open(os.getcwd() + "/2025/11/example.txt", "r") as f:
with open(os.getcwd() + "/AoC_private/2025/11/input.txt", "r") as f:
    input = f.read()
    input = input.split("\n")
    # input = []
    # for line in f.readlines():
    # input.append(int(line))
    # input = [int(line) for line in f.readlines()]
    # input = [line for line in f.readlines()]

# print(input)

# PART 1
solution_1 = 0

nodes = dict()
for line in input:
    line = line.replace(":", "")
    line = line.split(" ")
    nodes[line[0]] = line[1:]

graph = nx.DiGraph()

for node in nodes:
    for edge in nodes[node]:
        graph.add_edge(node, edge)

bla = list(nx.all_simple_paths(graph, "you", "out"))
solution_1 = len(bla)

### SOLUTION 1
print("Part One : " + str(solution_1))

submit(solution_1, part="a", day=11, year=2025)
