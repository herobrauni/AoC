# Advent of Code Year 2024 Day 15 solution
# Author = brauni
# Date = 2024-12-15

import copy
import os
from aocd import submit
from aocd.models import Puzzle
puzzle = Puzzle(year=2024, day=15)

# with open(os.getcwd() + "/2024/15/example.txt", 'r') as f:
with open(os.getcwd() + "/AoC_private/2024/15/input.txt", 'r') as f:
    input = f.read()
    input = input.split("\n\n")

grid = input[0].split("\n")
moves = input[1].replace("\n", "")

g = {}
for n, line in enumerate(grid):
    for m, x in [(m, y) for m, y in enumerate(line)]:
        g[complex(m, n)] = x
        if x == "@":
            start = complex(m, n)

dirs = {
    "<": -1,
    ">": 1,
    "v": 1j,
    "^": -1j
}


def push(f, startbox, direction):
    q = []
    q.append(startbox)
    while len(q) > 0:
        box = q.pop()
        if box + direction in f:
            if f[box + direction] == ".":
                f[box] = "."
                f[box+direction] = "O"
            elif f[box+direction] == "O":
                q.append(box)
                q.append(box+direction)
            elif f[box+direction] == "#":
                return f
    return f


# PART 1
solution_1 = 0
f = copy.deepcopy(g)
pos = start
for x in moves:
    # print(pos, x)
    move = dirs[x]
    if pos+move in f:
        # print(pos, f[pos+move])
        if f[pos+move] == ".":
            f[pos] = "."
            f[pos+move] = "@"
            pos = pos+move
        elif f[pos+move] == "O":
            f = push(f, pos+move, move)
            if f[pos+move] == ".":
                f[pos] = "."
                f[pos+move] = "@"
                pos = pos+move

for x in f:
    if f[x] == "O":
        solution_1 += int(x.real) + int(x.imag)*100

# SOLUTION 1
print("Part One : " + str(solution_1))

submit(solution_1, part="a", day=15, year=2024)
