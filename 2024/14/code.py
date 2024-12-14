# Advent of Code Year 2024 Day 14 solution
# Author = brauni
# Date = 2024-12-14
from collections import Counter
import copy
import functools
import re
import os
from aocd import submit
from aocd.models import Puzzle
puzzle = Puzzle(year=2024, day=14)


# with open(os.getcwd() + "/2024/14/example.txt", 'r') as f:
with open(os.getcwd() + "/AoC_private/2024/14/input.txt", 'r') as f:
    inp = f.read()
    inp = inp.split("\n")


# @functools.cache
def one_sec(g, h, w, moves=1):
    f = copy.deepcopy(g)
    for x in f:
        f[x] = move(f[x], x[1], h, w, moves)
    return f


@functools.cache
def move(start, x, h, w, moves):
    t = start + x * moves
    return complex(t.real % w, t.imag % h)


def calc_p1(g, h, w):
    tl, tr, bl, br = 0, 0, 0, 0
    for z in g.values():
        # top left
        if z.real < w // 2 and z.imag < h//2:
            tl += 1
        # top right
        if z.real > w // 2 and z.imag < h//2:
            tr += 1
        # bottom left
        if z.real < w // 2 and z.imag > h//2:
            bl += 1
        # bottom right
        if z.real > w // 2 and z.imag > h//2:
            br += 1
    return tl*tr*br*bl


def print_grid(d, h, w):
    for i in range(h):
        for j in range(w):
            if complex(j, i) in d.values():
                print("#", end="")
            else:
                print(".", end="")
        print("")
    # return True


print(inp)

g = {}
for line in inp:
    start = re.findall(r'p=(\d+,\d+)', line)[0].split(",")
    start = complex(int(start[0]), int(start[1]))

    v = re.findall(r'v=(\-?\d+,\-?\d+)', line)[0].split(",")
    v = complex(int(v[0]), int(v[1]))
    g[(start, v)] = start


h = 103  # 7
w = 101  # 11

solution_1 = calc_p1(one_sec(g, h, w, moves=100), h, w)
# SOLUTION 1
print("Part One : " + str(solution_1))

submit(solution_1, part="a", day=14, year=2024)


f = copy.deepcopy(g)

for i in range(h*w):
    f = one_sec(g, h, w, moves=i)
    columns = max(Counter([x.real for x in f.values()]).values())
    lines = max(Counter([x.imag for x in f.values()]).values())
    if lines > 20 and columns > 20:
        print(i)
        print_grid(f, h, w)
        print(i)

solution_2 = i

# SOLUTION 2
print("Part Two : " + str(solution_2))

submit(solution_2, part="b", day=14, year=2024)
