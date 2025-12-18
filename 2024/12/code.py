# Advent of Code Year 2024 Day 12 solution
# Author = brauni
# Date = 2024-12-12

import os
from aocd import submit
from aocd.models import Puzzle
puzzle = Puzzle(year=2024, day=12)


# with open(os.getcwd() + "/2024/12/example.txt", 'r') as f:
with open(os.getcwd() + "/AoC_private/2024/12/input.txt", 'r') as f:
    input = f.read()
    input = input.split("\n")

# print(input)

# PART 1
solution_1 = 0
g = {}
for n, line in enumerate(input):
    for m, x in [(m, y) for m, y in enumerate(line)]:
        g[complex(m, n)] = x


def iterative_flood_fill(start, g, pos):
    if (pos not in g):
        return
    if (g[pos] != start):
        return
    f = set()
    q = []
    f.add(pos)
    q.append(pos)
    while len(q) > 0:
        pos = q[0]
        del q[0]
        for dir in [1, -1, 1j, -1j]:
            if pos+dir in g and pos+dir not in f:
                if g[pos+dir] == start:
                    f.add(pos+dir)
                    q.append(pos+dir)
    return f


def neighbours(x, g):
    y = []
    for pos in x:
        for dir in [(1, 'right'), (-1, 'left'), (1j, 'down'), (-1j, 'up')]:
            if pos+dir[0] in g:
                if g[pos+dir[0]] != g[pos]:
                    y.append((pos+dir[0], dir[1]))
            else:
                y.append((pos+dir[0], dir[1]))
    return y


def iff_p2(g, pos):
    f = set()
    q = []
    f.add(pos)
    q.append(pos)
    while len(q) > 0:
        pos = q[0]
        del q[0]
        for dir in [1, -1, 1j, -1j]:
            if (pos[0]+dir, pos[1]) in g and (pos[0]+dir, pos[1]) not in f:
                f.add((pos[0]+dir, pos[1]))
                q.append((pos[0]+dir, pos[1]))
    return f


f = []
for k in g:
    f.append(iterative_flood_fill(g[k], g, k))

ff = []
for x in f:
    if x not in ff:
        ff.append(x)
f = [list(x) for x in ff]


solution_1 = 0
for x in f:
    area = len(x)
    perimeter = neighbours(x, g)
    # print(g[x[0]], area, len(perimeter))
    solution_1 += area*len(perimeter)

# SOLUTION 1
print("Part One : " + str(solution_1))

submit(solution_1, part="a", day=12, year=2024)


# PART 2
solution_2 = 0
for x in f:
    area = len(x)
    p = neighbours(x, g)
    t = []
    for pp in p:
        t.append(iff_p2(p, pp))
    tt = []
    for xxx in t:
        if xxx not in tt:
            tt.append(xxx)
    # print(g[x[0]], area, len(tt))
    solution_2 += area*len(tt)


# SOLUTION 2
print("Part Two : " + str(solution_2))

submit(solution_2, part="b", day=12, year=2024)
