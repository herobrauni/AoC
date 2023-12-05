# Advent of code Year 2022 Day 22 solution
# Author = brauni
# Date = 2022-12-27
"https://adventofcode.com/2022/day/22"

import re
from collections import Counter
import copy
import os
import math
import numpy as np
from operator import add

solution_1, solution_2 = 0, 0

# with open(os.getcwd() + "/2022/22/example.txt", 'r') as f:
with open(os.getcwd() + "/AoC_private/2022/22/input.txt", "r") as f:
    input = f.read()
    input = input.split("\n\n")
    # input = []
    # for line in f.readlines():
    # input.append(int(line))
    # input = [int(line) for line in f.readlines()]
    # input = [line for line in f.readlines()]

# PART 0


print(input)

instructions = input[1]
instructions = [x for x in re.split(r"(\d+)", instructions) if x != ""]
input = input[0].split("\n")
w_max = max([len(x) for x in input])
for i in range(len(input)):
    while len(input[i]) < w_max:
        input[i] = "".join([input[i], " "])
grid = np.zeros(len(input) * w_max, dtype=str)  # .reshape(len(input),len(input[0]))

input_flat = "".join(input)
for i, x in enumerate(input_flat):
    # print(i,x)
    grid[i] = x

grid = grid.reshape(len(input), w_max)

grid_path = copy.deepcopy(grid)
# PART 1
for line in grid:
    print("".join(line))

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
d = 0
direction_markers = [">", "v", "<", "^"]

for i in range(len(grid[0])):
    if grid[0][i] == ".":
        s = i
        break

pos = (0, s)


def find_wrap(grid, pos, d):
    og_pos = pos
    if d == (0, 1):
        pos = (pos[0], 0)
        while grid[pos] == " ":
            pos = a(pos, d)
        if grid[pos] == "#":
            return og_pos
        else:
            return pos
    if d == (0, -1):
        pos = (pos[0], len(grid[pos[0]]) - 1)
        while grid[pos] == " ":
            pos = a(pos, d)
        if grid[pos] == "#":
            return og_pos
        else:
            return pos
    if d == (1, 0):
        # print(d, pos)
        pos = (0, pos[1])
        while grid[pos] == " ":
            pos = a(pos, d)
            # print(d, pos, grid[pos])
        if grid[pos] == "#":
            return og_pos
        else:
            return pos
    if d == (-1, 0):
        pos = (len(grid[pos[1]]) - 1, pos[1])
        while grid[pos] == " ":
            pos = a(pos, d)
        if grid[pos] == "#":
            return og_pos
        else:
            return pos


a = lambda pos, d: tuple(map(add, pos, d))
# find_wrap(grid, (5,11), (1,0))

# a((0,10), (0,1))


for instr in instructions:
    # print(instr, pos, directions[d])
    if re.search("\d", instr) != None:
        instr = int(instr)
        for i in range(instr):
            # print(instr, pos, directions[d])
            grid_path[pos] = direction_markers[d]
            if a(pos, directions[d])[0] not in range(len(grid)) or a(
                pos, directions[d]
            )[1] not in range(w_max):
                pos = find_wrap(grid, pos, directions[d])
            elif grid[a(pos, directions[d])] == " ":
                pos = find_wrap(grid, pos, directions[d])
            elif (
                grid[a(pos, directions[d])] == "."
            ):  # or grid[a(pos,directions[d])] in direction_markers:
                pos = a(pos, directions[d])
            elif grid[a(pos, directions[d])] == "#":
                break
    else:
        if instr == "R":
            d = d + 1 if d < 3 else 0
        elif instr == "L":
            d = d - 1 if d > 0 else 3

solution_1 = 1000 * (pos[0] + 1) + 4 * (pos[1] + 1) + d


def move_cube2(cs, pos, d, side):
    og_pos = pos
    og_side = side
    og_cs = cs
    # n = 0
    match d:
        case (0, 1):  # right
            # if d == (0,1): # right
            n = cs[side][a(pos, d)]
            while cs[n][1][0] != side:
                cs[n] = np.rot90(cs[n])
            if cs[n][(pos[0], 1)] == 0:
                return (pos[0], 1), n, cs
            elif cs[n][(pos[0], 1)] == 8:
                return og_pos, og_side, og_cs
        case (0, -1):  # left
            # elif d == (0,-1): # left
            n = cs[side][a(pos, d)]
            while cs[n][1][-1] != side:
                cs[n] = np.rot90(cs[n])
            if cs[n][(pos[0], len(cs[n][pos[0]]) - 2)] == 0:
                return (pos[0], len(cs[n][pos[0]]) - 2), n, cs
            elif cs[n][(pos[0], len(cs[n][pos[0]]) - 2)] == 8:
                return og_pos, og_side, og_cs
        case (1, 0):  # down
            # elif d == (1,0): # down
            n = cs[side][a(pos, d)]
            while cs[n][0][1] != side:
                cs[n] = np.rot90(cs[n])
            if cs[n][(1, pos[1])] == 0:
                return (1, pos[1]), n, cs
            elif cs[n][(1, pos[1])] == 8:
                return og_pos, og_side, og_cs
        case (-1, 0):  # up
            # elif d == (-1,0): # up
            n = cs[side][a(pos, d)]
            while cs[n][-1][1] != side:
                cs[n] = np.rot90(cs[n])
            if cs[n][(len(cs[n]) - 2, pos[1])] == 0:
                return (len(cs[n]) - 2, pos[1]), n, cs
            elif cs[n][(len(cs[n]) - 2, pos[1])] == 8:
                return og_pos, og_side, og_cs
    return False


with open(os.getcwd() + "/AoC_private/2022/22/input.txt", "r") as f:
    input = f.read()
    input = input.split("\n\n")


directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
d = 0

instructions = input[1]
instructions = [x for x in re.split(r"(\d+)", instructions) if x != ""]
input = input[0].split("\n")
w_max = max([len(x) for x in input])
for i in range(len(input)):
    while len(input[i]) < w_max:
        input[i] = "".join([input[i], " "])
grid = np.zeros(len(input) * w_max, dtype=int)  # .reshape(len(input),len(input[0]))

input_flat = "".join(input)
for i, x in enumerate(input_flat):
    # print(i,x)
    if x == "#":
        grid[i] = 8
    elif x == ".":
        grid[i] = 0
    elif x == " ":
        grid[i] = -1

grid = grid.reshape(len(input), w_max)

tmp = int(len(grid) // 4)
side_1 = np.array([x[tmp:-tmp] for x in grid[:tmp]])
side_1 = np.pad(side_1, 1)
side_1[0] = np.full_like(side_1[0], 6)  # up
side_1 = np.rot90(side_1)
side_1[0] = np.full_like(side_1[0], 2)  # right
side_1 = np.rot90(side_1)
side_1[0] = np.full_like(side_1[0], 3)  # down
side_1 = np.rot90(side_1)
side_1[0] = np.full_like(side_1[0], 5)  # left
side_1 = np.rot90(side_1)

np.array([x[tmp * 2 :] for x in grid[:tmp]])
side_2 = np.array([x[tmp * 2 :] for x in grid[:tmp]])
side_2 = np.pad(side_2, 1)
side_2[0] = np.full_like(side_2[0], 6)
side_2 = np.rot90(side_2)
side_2[0] = np.full_like(side_2[0], 4)
side_2 = np.rot90(side_2)
side_2[0] = np.full_like(side_2[0], 3)
side_2 = np.rot90(side_2)
side_2[0] = np.full_like(side_2[0], 1)
side_2 = np.rot90(side_2)

side_3 = np.array([x[tmp:-tmp] for x in grid[tmp : tmp * 2]])
side_3 = np.pad(side_3, 1)
side_3[0] = np.full_like(side_3[0], 1)
side_3 = np.rot90(side_3)
side_3[0] = np.full_like(side_3[0], 2)
side_3 = np.rot90(side_3)
side_3[0] = np.full_like(side_3[0], 4)
side_3 = np.rot90(side_3)
side_3[0] = np.full_like(side_3[0], 5)
side_3 = np.rot90(side_3)

side_4 = np.array([x[tmp:-tmp] for x in grid[tmp * 2 : tmp * 3]])
side_4 = np.pad(side_4, 1)
side_4[0] = np.full_like(side_4[0], 3)
side_4 = np.rot90(side_4)
side_4[0] = np.full_like(side_4[0], 2)
side_4 = np.rot90(side_4)
side_4[0] = np.full_like(side_4[0], 6)
side_4 = np.rot90(side_4)
side_4[0] = np.full_like(side_4[0], 5)
side_4 = np.rot90(side_4)

side_5 = np.array([x[:tmp] for x in grid[tmp * 2 : tmp * 3]])
side_5 = np.pad(side_5, 1)
side_5[0] = np.full_like(side_5[0], 3)
side_5 = np.rot90(side_5)
side_5[0] = np.full_like(side_5[0], 4)
side_5 = np.rot90(side_5)
side_5[0] = np.full_like(side_5[0], 6)
side_5 = np.rot90(side_5)
side_5[0] = np.full_like(side_5[0], 1)
side_5 = np.rot90(side_5)

side_6 = np.array([x[:tmp] for x in grid[tmp * 3 : tmp * 4]])
side_6 = np.pad(side_6, 1)
side_6[0] = np.full_like(side_6[0], 5)
side_6 = np.rot90(side_6)
side_6[0] = np.full_like(side_6[0], 4)
side_6 = np.rot90(side_6)
side_6[0] = np.full_like(side_6[0], 2)
side_6 = np.rot90(side_6)
side_6[0] = np.full_like(side_6[0], 1)
side_6 = np.rot90(side_6)


# side_1 = np.insert(side_1,0,np.array([2]*(tmp+1+2)))
# side_1

cube_sides = [[], side_1, side_2, side_3, side_4, side_5, side_6]
# cube_sides = [np.pad(x, pad_width=1, mode='constant', constant_values='-1') for x in cube_sides]
side_0 = [
    np.array([1, 2, 3, 4]),
    np.array([5, 6, 7, 8]),
    np.array([9, 10, 11, 12]),
    np.array([13, 14, 15, 16]),
]


cs = [side_0, side_1, side_2, side_3, side_4, side_5, side_6]

for i in range(1, len(cs)):
    cs[i][0][0] = -1
    cs[i][0][-1] = -1
    cs[i][-1][0] = -1
    cs[i][-1][-1] = -1

cube_sides_org = copy.deepcopy(cs)

side = 1
for i in range(len(cs[side][1])):
    if cs[side][1][i] == 0:
        s = i
        break
pos = (1, s)


for instr in instructions:
    # print(instr, pos, directions[d])
    if re.search("\d", instr) != None:
        instr = int(instr)
        for i in range(instr):
            # print(side, (pos[0]-1, pos[1]-1), instr, directions[d])
            # print(cs[side])

            if cs[side][a(pos, directions[d])] not in [0, 8]:
                # print("wrapping")
                pos, side, cs = move_cube2(
                    cs, pos, directions[d], side
                )  # og_pos, og_side, og_cs
            elif (
                cs[side][a(pos, directions[d])] == 0
            ):  # or grid[a(pos,directions[d])] in direction_markers:
                pos = a(pos, directions[d])
            elif cs[side][a(pos, directions[d])] == 8:
                break
    else:
        # print(side, (pos[0]-1, pos[1]-1), instr)
        if instr == "R":
            d = d + 1 if d < 3 else 0
        elif instr == "L":
            d = d - 1 if d > 0 else 3
cs[side][pos] = 9

# bla = np.array([1,2,3,4,5,6,7,8,9])
# bla = np.resize(bla, (3,3))
# bla = np.pad(bla, 1)
# bla[0] = np.full_like(bla[0], 2)
# bla


while cs[side][0, 1] != cube_sides_org[side][0, 1]:
    cs[side] = np.rot90(cs[side])
    d = d - 1 if d > 0 else 3

for i in range(1, len(cs)):
    while cs[i][0, 1] != cube_sides_org[i][0, 1]:
        cs[i] = np.rot90(cs[i])

for i in range(1, len(cs)):
    cs[i] = cs[i][1:-1, 1:-1]

for i in range(len(cs[side])):
    for j in range(len(cs[side][i])):
        if cs[side][i][j] == 9:
            s1, s2 = i, j
            break


# side_1 = np.array([x[tmp*2+2:-tmp-1] for x in grid[:tmp+1]])
tmp = len(cs[side])
match side:
    case 1:
        offset = (1, tmp + 1)  # 1,51
    case 2:
        offset = (1, tmp * 2 + 1)  # 1,101
    case 3:
        offset = (tmp + 1, tmp + 1)  # 51,51
    case 4:
        offset = (tmp * 2 + 1, tmp + 1)  # 101,51
    case 5:
        offset = (tmp * 2 + 1, 1)  # 101,1
    case 6:
        offset = (tmp * 3 + 1, 1)  # 151,1


final_pos = a((s1, s2), offset)
solution_2 = 1000 * (final_pos[0]) + 4 * (final_pos[1]) + d


# SOLUTIONS

print("Part One : " + str(solution_1) + "\nPart Two : " + str(solution_2))
