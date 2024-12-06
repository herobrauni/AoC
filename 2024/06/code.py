# Advent of Code Year 2024 Day 6 solution
# Author = brauni
# Date = 2024-12-06

import copy
import re
import os
from aocd import submit
from aocd.models import Puzzle
puzzle = Puzzle(year=2024, day=6)

# with open(os.getcwd() + "/2024/06/example.txt", 'r') as f:
with open(os.getcwd() + "/AoC_private/2024/06/input.txt", 'r') as f:
    input = f.read()
    input = input.split("\n")
    # input = []
    # for line in f.readlines():
    # input.append(int(line))
    # input = [int(line) for line in f.readlines()]
    # input = [line for line in f.readlines()]

print(input)
g = {}
for n, line in enumerate(input):
    for m, x in [(m, y) for m, y in enumerate(line)]:
        g[complex(m, n)] = x
        if x != "." and x != "#":
            start = complex(m, n)
            g[start] = "X"

directions = [complex(0, -1), complex(1, 0), complex(0, 1), complex(-1, 0)]

# PART 1
solution_1 = 0
pos = start

dir = 0
while pos in g.keys():
    while (pos+directions[dir]) in g.keys() and g[pos+directions[dir]] != "#":
        pos = pos + directions[dir]
        g[pos] = "X"
    if (pos+directions[dir]) not in g.keys():
        break
    dir = (dir + 1) % 4

solution_1 = sum([1 for x in g.keys() if g[x] == "X"])

# SOLUTION 1
print("Part One : " + str(solution_1))

submit(solution_1, part="a", day=6, year=2024)


# PART 2
solution_2 = 0
g = {}
for n, line in enumerate(input):
    for m, x in [(m, y) for m, y in enumerate(line)]:
        g[complex(m, n)] = x
g[start] = "."

for z in g.keys():
    f = copy.deepcopy(g)
    if g[z] != "#":
        g[z] = "O"
    pos = start
    loop = False
    dir = 0
    for i in range(10000):
        while (pos+directions[dir]) in g.keys() and g[pos+directions[dir]] == ".":
            pos = pos + directions[dir]
        if (pos+directions[dir]) not in g.keys():
            break
        dir = (dir + 1) % 4
    else:
        print("loop for: ", z)
        loop = True
    solution_2 += 1 if loop else 0
    if g[z] != "#":
        g[z] = "."


# print(loop)

# SOLUTION 2
print("Part Two : " + str(solution_2))

submit(solution_2, part="b", day=6, year=2024)
