# Advent of code Year 2021 Day 15 solution
# Author = brauni
# Date = 2021-12-15
"https://adventofcode.com/2021/day/15"

import re
from collections import Counter
import copy
import os
import math
import networkx

solution_1, solution_2 = 0, 0

# with open(os.getcwd() + "\\2021\\15\\example.txt", 'r') as f:
with open(os.getcwd() + "\\2021\\15\\input.txt", 'r') as f:
    input = f.read()
    input = input.split("\n")

# PART 0
# Convert all to single ints
inp = []
for line in input:
    inp.append(list(map(int, str(line))))

input = copy.deepcopy(inp)


# Creates a bigger array by copying the input array factor times to the right and to the bottom
# each time the array is copied, the values are incremented by 1, if the value is 9, it wraps around to 1
# returns the new array and the last element of the new array
def create_bigger_input_by_factor(input, factor):
    bigger_input = copy.deepcopy(input)
    for x in range(len(input), len(input)*factor):
        bigger_input.append(
            [x+1 if x < 9 else 1 for x in bigger_input[x-len(input)]])
    width = len(bigger_input[0])
    for x in range(factor-1):
        for i in range(len(bigger_input)):
            for j in range(x*width, (x+1)*width):
                # print(j)
                increased_number = bigger_input[i][j] + \
                    1 if bigger_input[i][j] < 9 else 1
                bigger_input[i].append(increased_number)
    return bigger_input, len(bigger_input)*len(bigger_input[0])-1


# Creates a graph for an array, each node is the number of the field in the array
# each edge is weighted by the value of the field in the array
def create_graph(input):
    g = networkx.DiGraph()
    g.add_nodes_from(range(0, len(input)*len(input[0])))

    for i in range(len(input)):
        for j in range(len(input[0])):
            position = i*len(input[0]) + j
            up = position - \
                len(input[0]) if position >= len(input[0]) else None
            down = position + len(input[0]) if i < len(input) - 1 else None
            left = position - 1 if position % len(input[0]) != 0 else None
            right = position + 1 if j < len(input[0]) - 1 else None
            if down is not None:
                g.add_edge(position, down, weight=input[i+1][j])
            if right is not None:
                g.add_edge(position, right, weight=input[i][j+1])
            if left is not None:
                g.add_edge(position, left, weight=input[i][j-1])
            if up is not None:
                g.add_edge(position, up, weight=input[i-1][j])
    return g


# Create the graph from the input array and find the shortest path from the top left to the bottom right
g = create_graph(input)
solution_1 = networkx.dijkstra_path_length(g, 0, len(input)*len(input[0])-1)

# PART 2
# increase array and create a new graph
# find the shortest path from the top left to the bottom right
p2_input, p2_last_element = create_bigger_input_by_factor(input, 5)
p2_graph = create_graph(p2_input)
solution_2 = networkx.dijkstra_path_length(p2_graph, 0, p2_last_element)


# SOLUTIONS
print("Part One : " + str(solution_1) + "\nPart Two : " + str(solution_2))
