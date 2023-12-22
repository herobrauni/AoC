# Advent of code Year 2023 Day 22 solution
# Author = brauni
# Date = 2023-12-22
"https://adventofcode.com/2023/day/22"

import re
from collections import Counter
import copy
import os
import math
import numpy as np

solution_1, solution_2 = 0, 0

with open(os.getcwd() + "/AoC_private/2023/22/input.txt", "r") as f:
    # with open(os.getcwd() + "/2023/22/example.txt", "r") as f:
    input = f.read()
    input = input.split("\n")


# PART 0


def into_grid(grid, coords, tttt):
    x, y, z, xx, yy, zz = coords
    for i in range(x, xx + 1):
        for j in range(y, yy + 1):
            for g in range(z, zz + 1):
                grid[i, j, g] = tttt
    return grid


def calc_falling(grid, dd, tttt):
    g2 = copy.deepcopy(grid)
    d = copy.deepcopy(dd)
    coords = d[tttt]
    g2 = into_grid(g2, coords, 0)
    del d[tttt]
    falling = set()
    moved = True
    while moved:
        moved = False
        for tttt in d:
            x, y, z, xx, yy, zz = d[tttt]
            if z - 1 <= 0:
                continue
            for i in range(x, xx + 1):
                for j in range(y, yy + 1):
                    if g2[i, j, z - 1] == 0:
                        continue
                    else:
                        break
                else:
                    continue
                break
            else:
                g2 = into_grid(g2, d[tttt], 0)
                d[tttt] = (x, y, z - 1, xx, yy, zz - 1)
                g2 = into_grid(g2, d[tttt], tttt)
                falling.add(tttt)
                moved = True
    return falling


r = 350
grid = np.zeros((r, r, r))
tttt = 0
d = {}
for line in input:
    tttt += 1
    a, b = line.split("~")
    x, y, z = (int(_) for _ in a.split(","))
    xx, yy, zz = (int(_) for _ in b.split(","))
    d[tttt] = (x, y, z, xx, yy, zz)
    grid = into_grid(grid, (x, y, z, xx, yy, zz), tttt)

moved = True
while moved:
    moved = False
    for tttt in d:
        x, y, z, xx, yy, zz = d[tttt]
        if z - 1 <= 0:
            continue
        for i in range(x, xx + 1):
            for j in range(y, yy + 1):
                if grid[i, j, z - 1] == 0:
                    continue
                else:
                    break
            else:
                continue
            break
        else:
            grid = into_grid(grid, d[tttt], 0)
            d[tttt] = (x, y, z - 1, xx, yy, zz - 1)
            grid = into_grid(grid, d[tttt], tttt)
            moved = True


# PART 1
s = {}
for t in d:
    s[t] = set()
    x, y, z, xx, yy, zz = d[t]
    for i in range(x, xx + 1):
        for j in range(y, yy + 1):
            if grid[i, j, zz + 1] != 0:
                s[t].add(int(grid[i, j, zz + 1]))

values = []
for z in s:
    v = s[z]
    values += v
vc = Counter(values)
desintegrate = set()
for x in s:
    if len(s[x]) == 0:
        desintegrate.add(x)
    for y in s[x]:
        if vc[y] == 1:
            break
    else:
        desintegrate.add(x)
solution_1 = len(desintegrate)


# PART 2


for i in d:
    solution_2 += len(calc_falling(grid, d, i))

# SOLUTIONS

print("Part One : " + str(solution_1) + "\nPart Two : " + str(solution_2))
