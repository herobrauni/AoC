# Advent of code Year 2022 Day 12 solution
# Author = brauni
# Date = 2022-12-12
"https://adventofcode.com/2022/day/12"

import re
from collections import Counter
import copy
import os
import math
import networkx

solution_1, solution_2 = 0, 0

# with open(os.getcwd() + "\\2022\\12\\example.txt", 'r') as f:
with open(os.getcwd() + "\\2022\\12\\input.txt", "r") as f:
    input = f.read()
    input = input.split("\n")

# PART 0
# Convert all to single ints
inp = []
for line in input:
    print(line)
    inp.append(list(line))

input = copy.deepcopy(inp)


print(input)


def create_graph(input):
    g = networkx.DiGraph()
    g.add_nodes_from(range(0, len(input) * len(input[0])))

    for i in range(len(input)):
        for j in range(len(input[0])):
            position = i * len(input[0]) + j
            # print(position)
            up = position - len(input[0]) if position >= len(input[0]) else None
            down = position + len(input[0]) if i < len(input) - 1 else None
            left = position - 1 if position % len(input[0]) != 0 else None
            right = position + 1 if j < len(input[0]) - 1 else None
            if down is not None and ord(input[i + 1][j]) <= ord(input[i][j]) + 1:
                g.add_edge(position, down, weight=1)
            if right is not None and ord(input[i][j + 1]) <= ord(input[i][j]) + 1:
                g.add_edge(position, right, weight=1)
            if left is not None and ord(input[i][j - 1]) <= ord(input[i][j]) + 1:
                g.add_edge(position, left, weight=1)
            if up is not None and ord(input[i - 1][j]) <= ord(input[i][j]) + 1:
                g.add_edge(position, up, weight=1)
    return g


for i in range(len(input)):
    for j in range(len(input[i])):
        if input[i][j] == "E":
            input[i][j] = "z"
            end = [i, j]
            break

for i in range(len(input)):
    for j in range(len(input[i])):
        if input[i][j] == "S":
            input[i][j] = "a"
            start = [i, j]
            break

# Create the graph from the input array and find the shortest path from the start left to the end
g = create_graph(input)
solution_1 = networkx.dijkstra_path_length(
    g, start[0] * len(input[0]) + start[1], end[0] * len(input[0]) + end[1]
)

solution_2 = solution_1  # we need a shorter path, so set this as the expectation
# PART 2
for i in range(len(input)):
    for j in range(len(input[i])):
        # run through the array, calculate path for each 'a', continue to next 'a' if no path found
        if input[i][j] == "a":
            try:
                temp = networkx.dijkstra_path_length(
                    g, i * len(input[0]) + j, end[0] * len(input[0]) + end[1]
                )
                solution_2 = temp if temp < solution_2 else solution_2
            except:
                pass
# SOLUTIONS

print("Part One : " + str(solution_1) + "\nPart Two : " + str(solution_2))
