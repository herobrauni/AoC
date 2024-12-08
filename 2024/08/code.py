# Advent of Code Year 2024 Day 8 solution
# Author = brauni
# Date = 2024-12-08

import numpy as np
import math
import itertools
import re
import os
from aocd import submit
from aocd.models import Puzzle
puzzle = Puzzle(year=2024, day=8)

# with open(os.getcwd() + "/2024/08/example.txt", 'r') as f:
with open(os.getcwd() + "/AoC_private/2024/08/input.txt", 'r') as f:
    input = f.read()
    input = input.split("\n")


print(input)
g = {}
f = {}
for n, line in enumerate(input):
    for m, x in [(m, y) for m, y in enumerate(line)]:
        g[(m, n)] = x
        if x != ".":
            if x not in f.keys():
                f[x] = [np.array([m, n])]
            else:
                f[x].append(np.array([m, n]))
# PART 1
solution_1 = 0
for x in f.keys():
    if len(f[x]) > 1:
        for c in itertools.combinations(f[x], 2):
            v1, v2 = c[0]-c[1], c[1]-c[0]
            c1, c2 = c[0]+v1, c[1]+v2
            c1, c2 = (int(c1[0]), int(c1[1])), (int(c2[0]), int(c2[1]))
            if c1 in g.keys():
                g[c1] = "#"
            if c2 in g.keys():
                g[c2] = "#"

solution_1 = sum([1 for x in g.values() if x == "#"])

# SOLUTION 1
print("Part One : " + str(solution_1))

submit(solution_1, part="a", day=8, year=2024)


# PART 2
solution_2 = 0
g = {}
f = {}
for n, line in enumerate(input):
    for m, x in [(m, y) for m, y in enumerate(line)]:
        g[(m, n)] = x
        if x != ".":
            if x not in f.keys():
                f[x] = [np.array([m, n])]
            else:
                f[x].append(np.array([m, n]))


for x in f.keys():
    if len(f[x]) > 1:
        for y in f[x]:
            g[(int(y[0]), int(y[1]))] = "#"
        for c in itertools.combinations(f[x], 2):
            v1, v2 = c[0]-c[1], c[1]-c[0]
            gcd = math.gcd(int(v1[0]), int(v1[1]))
            v1, v2 = np.array([int(v1[0])//gcd, int(v1[1])//gcd]
                              ), np.array([int(v2[0])//gcd, int(v2[1])//gcd])
            c1, c2 = c[0]+v1, c[1]+v2
            while True:
                if (int(c1[0]), int(c1[1])) in g.keys():
                    g[(int(c1[0]), int(c1[1]))] = "#"
                else:
                    break
                c1 += v1
            while True:
                if (int(c2[0]), int(c2[1])) in g.keys():
                    g[(int(c2[0]), int(c2[1]))] = "#"
                else:
                    break
                c2 += v2
solution_2 = sum([1 for x in g.values() if x == "#"])

# SOLUTION 2
print("Part Two : " + str(solution_2))

submit(solution_2, part="b", day=8, year=2024)
