# Advent of code Year 2022 Day 23 solution
# Author = brauni
# Date = 2022-12-27
"https://adventofcode.com/2022/day/23"

import re
from collections import Counter, deque
import copy
import os
import math
import numpy as np
from operator import add

solution_1, solution_2 = 0, 0

# with open(os.getcwd() + "/2022/23/example.txt", 'r') as f:
with open(os.getcwd() + "/AoC_private/2022/23/input.txt", "r") as f:
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


def remove_padding(g):
    for y in range(4):
        # grid
        tbr = 0
        for i in range(len(g)):
            # print(''.join(str(grid[i])))
            if len(np.where(g[i] == 0)[0]) == len(g[i]):
                tbr += 1
            else:
                break
        g = g[tbr:]
        g = np.rot90(g)
    return g


# print(input)


grid = np.zeros(
    len(input) * len(input[0]), dtype=int
)  # .reshape(len(input),len(input[0]))

input_flat = "".join(input)
elf = 1
elfs = {}
for i, x in enumerate(input_flat):
    # print(i,x)
    if x == "#":
        grid[i] = elf
        elfs[elf] = ["X", deque(["N", "S", "W", "E"])]
        elf += 1
    elif x == ".":
        grid[i] = 0
    elif x == " ":
        grid[i] = -1

grid = grid.reshape(len(input), len(input[0]))


north = (-1, 0)
south = (1, 0)
west = (0, -1)
east = (0, 1)

ne = a(north, east)
nw = a(north, west)
se = a(south, east)
sw = a(south, west)

directions = [north, south, west, east, ne, nw, se, sw]


yyy = 0
while True:
    grid = np.pad(grid, pad_width=1)
    result = np.where(grid != 0)
    elf_positions = list(zip(result[0], result[1]))

    grid_proposed_moves = np.zeros_like(grid)
    for elf in elf_positions:
        # FIRST HALF, CHECK ALL DIRECTIONS -> IF ALL EMPTY, DO NOTHING
        for d in directions:
            if grid[a(elf, d)] != 0:
                break
        else:
            elfs[grid[elf]][0] = "X"
            continue
        move_found = False
        for d in elfs[grid[elf]][1]:
            match d:
                case "N":
                    for dd in [north, ne, nw]:
                        if grid[a(elf, dd)] != 0:
                            break
                    else:
                        move_found = d
                        break
                case "S":
                    for dd in [south, se, sw]:
                        if grid[a(elf, dd)] != 0:
                            break
                    else:
                        move_found = d
                        break
                case "W":
                    for dd in [west, nw, sw]:
                        if grid[a(elf, dd)] != 0:
                            break
                    else:
                        move_found = d
                        break
                case "E":
                    for dd in [east, ne, se]:
                        if grid[a(elf, dd)] != 0:
                            break
                    else:
                        move_found = d
                        break
        if move_found != False:
            elfs[grid[elf]][0] = move_found
            match move_found:
                case "N":
                    dd = north
                case "S":
                    dd = south
                case "W":
                    dd = west
                case "E":
                    dd = east
            grid_proposed_moves[a(elf, dd)] = grid_proposed_moves[a(elf, dd)] + 1
        else:
            elfs[grid[elf]][0] = "X"

    if all([True if elfs[x][0] == "X" else False for x in elfs]):
        solution_2 = yyy + 1
        break

    if yyy == 10:
        bla = remove_padding(grid)
        result = np.where(bla == 0)
        solution_1 = len(list(zip(result[0], result[1])))

    # SECOND HALF, ACTUALLY MOVING
    for elf in elf_positions:
        d = elfs[grid[elf]][0]
        e = grid[elf]
        match d:
            case "N":
                dd = north
            case "S":
                dd = south
            case "W":
                dd = west
            case "E":
                dd = east
            case "X":
                continue
        if grid_proposed_moves[a(elf, dd)] <= 1:
            grid[elf] = 0
            grid[a(elf, dd)] = e

    # rotate directions for next round
    for key in elfs:
        elfs[key][1].rotate(-1)

    yyy += 1

# SOLUTIONS

print("Part One : " + str(solution_1) + "\nPart Two : " + str(solution_2))
