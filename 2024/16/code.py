# Advent of Code Year 2024 Day 16 solution
# Author = brauni
# Date = 2024-12-16

import networkx as nx
import sys
import os
from aocd import submit
from aocd.models import Puzzle
puzzle = Puzzle(year=2024, day=16)


# with open(os.getcwd() + "/2024/16/example.txt", 'r') as f:
with open(os.getcwd() + "/AoC_private/2024/16/input.txt", 'r') as f:
    input = f.read()
    input = input.split("\n")

# print(input)
g = {}
for n, line in enumerate(input):
    for m, x in [(m, y) for m, y in enumerate(line)]:
        if x != "#":
            g[complex(m, n)] = x
            if x == "S":
                start = complex(m, n)
            if x == "E":
                end = complex(m, n)


def create_maze_graph(nodes):
    G = nx.DiGraph()

    for pos in nodes:
        for dir in [-1, 1, -1j, 1j]:
            next_pos = pos + dir
            if next_pos in nodes:
                for from_dir in [-1, 1, -1j, 1j]:
                    from_node = (pos, from_dir)
                    to_node = (next_pos, dir)
                    # Weight is 1 if same direction, 1001 if turning
                    weight = 1 if from_dir == dir else 1001
                    G.add_edge(from_node, to_node, weight=weight)
    return G


# Example usage:
G = create_maze_graph(g)

solution_1 = sys.maxsize
for dir in [1, -1, 1j, -1j]:
    try:
        t = nx.shortest_path_length(G, (start, 1), (end, dir), weight='weight')
    except nx.NetworkXNoPath:
        continue
    solution_1 = t if t < solution_1 else solution_1

# SOLUTION 1
print("Part One : " + str(solution_1))

submit(solution_1, part="a", day=16, year=2024)

# PART 2
all_paths = set()

for dir in [1, -1, 1j, -1j]:
    try:
        t = nx.shortest_path_length(G, (start, 1), (end, dir), weight='weight')
    except nx.NetworkXNoPath:
        continue
    if t == solution_1:
        t2 = nx.all_shortest_paths(G, (start, 1), (end, dir), weight='weight')
        for x in t2:
            for y in x:
                all_paths.add(y[0])
solution_2 = len(all_paths)

# SOLUTION 1
print("Part Two : " + str(solution_2))

submit(solution_2, part="b", day=16, year=2024)
