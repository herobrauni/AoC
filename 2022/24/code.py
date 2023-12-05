# Advent of code Year 2022 Day 24 solution
# Author = brauni
# Date = 2022-12-27
"https://adventofcode.com/2022/day/24"

import re
from collections import Counter, deque
import copy
import os
import math
import numpy as np
from operator import add
import networkx as nx
from datetime import datetime

solution_1, solution_2 = 0, 0

# with open(os.getcwd() + "/2022/24/example.txt", 'r') as f:
with open(os.getcwd() + "/AoC_private/2022/24/input.txt", "r") as f:
    input = f.read()
    input = input.split("\n")
    # input = []
    # for line in f.readlines():
    # input.append(int(line))
    # input = [int(line) for line in f.readlines()]
    # input = [line for line in f.readlines()]


# PART 0
def a(a, b):
    return tuple(map(add, a, b))


def trans_numbers(x):
    match x:
        case -1:
            bla = "#"
        case 0:
            bla = "."
        case 1:
            bla = "<"
        case 2:
            bla = ">"
        case 3:
            bla = "^"
        case 4:
            bla = "v"
        case 5:
            bla = "X"
        case 6:
            bla = "E"
        case "#":
            bla = -1
        case ".":
            bla = 0
        case "<":
            bla = 1
        case ">":
            bla = 2
        case "^":
            bla = 3
        case "v":
            bla = 4
        case "X":
            bla = 5
        case "E":
            bla = 6
    return bla


def print_grid(grid):
    for line in grid:
        print("".join([str(trans_numbers(x)) for x in line]))


def move_single_storm(grid, pos, n):
    direction = grid[pos]
    match direction:
        case 1:
            # dd = (0,-1)
            pos = (pos[0], (pos[1] + (n * -1) % len(grid[pos[0]])) % len(grid[pos[0]]))
        case 2:
            # dd = (0, 1)
            pos = (pos[0], (pos[1] + n) % len(grid[pos[0]]))
        case 3:
            # dd = (-1, 0)
            pos = ((pos[0] + (n * -1) % len(grid)) % len(grid), pos[1])
        case 4:
            # dd = (1, 0)
            pos = ((pos[0] + n) % len(grid), pos[1])
    return pos


def move_storms(grid, n):
    start, end = find_start(grid), find_end(grid)
    grid = grid[1:-1, 1:-1]
    grid_after = np.zeros_like(grid)

    for i, line in enumerate(grid):
        grid_after[i] = [-1 if x == -1 else 0 for x in line]
    result = np.where(grid > 0)
    storms = list(zip(result[0], result[1]))
    for storm in storms:
        grid_after[move_single_storm(grid, storm, n)] = 5
    grid_after = np.pad(grid_after, pad_width=1, constant_values=-1)
    grid_after[start] = 0
    grid_after[end] = 0
    return grid_after


def print_route(grids, paths):
    for i, x in enumerate(paths):
        print(i)
        grids[i][x] = 6
        for line in grids[i]:
            print("".join([str(trans_numbers(x)) for x in line]))
        print()


def find_start(grid):
    for i in range(len(grid[0])):
        if grid[0][i] == 0:
            return (0, i)


def find_end(grid):
    for i in range(len(grid[-1])):
        if grid[-1][i] == 0:
            return (len(grid) - 1, i)


# print(input)
grid = np.zeros(len(input) * len(input[0]), dtype=int)

input_flat = "".join(input)

# < > ^ v = 1 2 3 4
for i, x in enumerate(input_flat):
    # print(i,x)
    grid[i] = trans_numbers(x)

grid = grid.reshape(len(input), len(input[0]))

start, end = find_start(grid), find_end(grid)

G = nx.DiGraph()

grids = {}
# for i in range(5000):
#     print(i)
grids[0] = move_storms(grid, 0)
startTime = datetime.now()

for y in range(len(grids[0])):
    for z in range(len(grids[0][y])):
        if grids[0][y][z] != 0:
            continue
        else:
            G.add_node((0, y, z))


i = 1
while True:
    # print(i)
    grids[i] = move_storms(grid, i)

    for y in range(len(grids[i])):
        for z in range(len(grids[i][y])):
            if grids[i][y][z] != 0:
                continue
            for d in [(1, 0), (-1, 0), (0, -1), (0, 1), (0, 0)]:
                prev = a((y, z), d)
                if prev[0] not in range(len(grids[0])) or prev[1] not in range(
                    len(grids[0][0])
                ):
                    continue
                if grids[i - 1][prev] == 0:
                    G.add_node((i, y, z))
                    G.add_edge((i - 1, prev[0], prev[1]), (i, y, z))

    if nx.has_path(G, (0, start[0], start[1]), (i, end[0], end[1])):
        solution_1 = i
        break
    i += 1

t1 = i

while True:
    # print(i)
    grids[i] = move_storms(grid, i)

    for y in range(len(grids[i])):
        for z in range(len(grids[i][y])):
            if grids[i][y][z] != 0:
                continue
            for d in [(1, 0), (-1, 0), (0, -1), (0, 1), (0, 0)]:
                prev = a((y, z), d)
                if prev[0] not in range(len(grids[0])) or prev[1] not in range(
                    len(grids[0][0])
                ):
                    continue
                if grids[i - 1][prev] == 0:
                    G.add_node((i, y, z))
                    G.add_edge((i - 1, prev[0], prev[1]), (i, y, z))

    if nx.has_path(G, (t1, end[0], end[1]), (i, start[0], start[1])):
        # solution_1 = i
        break
    i += 1

t2 = i

while True:
    # print(i)
    grids[i] = move_storms(grid, i)

    for y in range(len(grids[i])):
        for z in range(len(grids[i][y])):
            if grids[i][y][z] != 0:
                continue
            for d in [(1, 0), (-1, 0), (0, -1), (0, 1), (0, 0)]:
                prev = a((y, z), d)
                if prev[0] not in range(len(grids[0])) or prev[1] not in range(
                    len(grids[0][0])
                ):
                    continue
                if grids[i - 1][prev] == 0:
                    G.add_node((i, y, z))
                    G.add_edge((i - 1, prev[0], prev[1]), (i, y, z))

    if nx.has_path(G, (t2, start[0], start[1]), (i, end[0], end[1])):
        solution_2 = i
        break
    i += 1
print(datetime.now() - startTime)

print("Part One : " + str(solution_1) + "\nPart Two : " + str(solution_2))
