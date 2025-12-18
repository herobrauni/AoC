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
        z = m * 2
        if x == "#":
            g[complex(z, n)] = x
            g[complex(z+1, n)] = x
        if x == ".":
            g[complex(z, n)] = x
            g[complex(z+1, n)] = x
        if x == "O":
            g[complex(z, n)] = "["
            g[complex(z+1, n)] = "]"
        if x == "@":
            g[complex(z, n)] = "@"
            g[complex(z+1, n)] = "."
            start = complex(z, n)

dirs = {
    "<": -1,
    ">": 1,
    "v": 1j,
    "^": -1j
}


def push_horizontal(f, startbox, direction):
    q = []
    q.append(startbox)
    while len(q) > 0:
        box = q.pop()
        if box + direction in f:
            if direction in [1, -1]:
                if f[box + direction] == ".":
                    f[box+direction] = f[box]
                    f[box] = "."
                elif f[box+direction] == "[" or f[box+direction] == "]":
                    q.append(box)
                    q.append(box+direction)
                elif f[box+direction] == "#":
                    return f
    return f


def reccheck(f, startbox, direction):
    if f[startbox[0] + direction] == "." and f[startbox[1] + direction] == ".":
        return True
    elif f[startbox[0] + direction] == "#" or f[startbox[1] + direction] == "#":
        return False
    elif f[startbox[0] + direction] == "[" and f[startbox[1] + direction] == "]":
        return reccheck(f, [startbox[0] + direction, startbox[1]+direction], direction)
    elif f[startbox[0] + direction] == "]" and f[startbox[1] + direction] == ".":
        return reccheck(f, [startbox[0] + direction-1, startbox[0]+direction], direction)
    elif f[startbox[0] + direction] == "." and f[startbox[1] + direction] == "[":
        return reccheck(f, [startbox[1] + direction, startbox[1]+direction+1], direction)
    else:
        return reccheck(f, [startbox[0]+direction-1, startbox[0]+direction], direction) and reccheck(f, [startbox[1]+direction, startbox[1]+direction+1], direction)


def push_vertical(f, startbox, direction):
    q = []
    q.append(startbox)
    while len(q) > 0:
        box = q.pop()
        if f[box[0]+direction] == "." and f[box[1]+direction] == ".":
            f[box[0]+direction] = f[box[0]]
            f[box[1]+direction] = f[box[1]]
            f[box[0]] = "."
            f[box[1]] = "."
        else:
            q.append(box)
            if f[box[0]+direction] == "]":
                q.append([box[0]+direction-1, box[0]+direction])
            if f[box[1]+direction] == "[":
                q.append([box[1]+direction, box[1]+direction+1])
            elif f[box[0]+direction] == "[":
                q.append([box[0]+direction, box[1]+direction])

    return f


def pg(gg):
    for n, line in enumerate(grid):
        for m, x in [(m, y) for m, y in enumerate(line)]:
            z = m*2
            print(gg[complex(z, n)], end="")
            print(gg[complex(z+1, n)], end="")
        print("")


# PART 2
solution_2 = 0
f = copy.deepcopy(g)
pos = start
for x in moves:
    move = dirs[x]
    if pos+move in f:
        if f[pos+move] == ".":
            f[pos] = "."
            f[pos+move] = "@"
            pos = pos+move
        elif f[pos+move] == "[" or f[pos+move] == "]":
            if move in [1, -1]:
                f = push_horizontal(f, pos+move, move)
            else:
                startbox = [pos+move, pos+move+1] if f[pos+move] == "[" else [pos+move-1, pos+move]
                if reccheck(f, startbox, move):
                    f = push_vertical(f, startbox, move)
            if f[pos+move] == ".":
                f[pos] = "."
                f[pos+move] = "@"
                pos = pos+move
    # pg(f)

for x in f:
    if f[x] == "[":
        solution_2 += int(x.real) + int(x.imag)*100

# # SOLUTION 1
print("Part One : " + str(solution_2))

submit(solution_2, part="b", day=15, year=2024)
