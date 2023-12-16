# Advent of code Year 2023 Day 16 solution
# Author = brauni
# Date = 2023-12-16
"https://adventofcode.com/2023/day/16"

import re
from collections import Counter
import copy
import os
import math
import numpy as np
from functools import cache

solution_1, solution_2 = 0, 0

with open(os.getcwd() + "/AoC_private/2023/16/input.txt", "r") as f:
    # with open(os.getcwd() + "/2023/16/example.txt", "r") as f:
    input = f.read()
    input = input.split("\n")

# PART 0
print(input)
g = {}
for n, line in enumerate(input):
    for m, x in [(m, y) for m, y in enumerate(line)]:
        g[complex(m, n)] = x


def shine(todo):
    done = set()
    while todo:
        pos, dir = todo.pop()
        while not (pos, dir) in done:
            done.add((pos, dir))
            pos += dir
            match g.get(pos):
                case "|":
                    dir = 1j
                    todo.append((pos, -dir))
                case "-":
                    dir = -1
                    todo.append((pos, -dir))
                case "/":
                    dir = -complex(dir.imag, dir.real)
                case "\\":
                    dir = complex(dir.imag, dir.real)
                case None:
                    break
    return len(set(pos for pos, _ in done)) - 1


solution_1 = shine([(-1, 1)])

for dir in (1, 1j, -1, -1j):
    for pos in g:
        if pos - dir not in g:
            z = shine([(pos - dir, dir)])
            solution_2 = z if z > solution_2 else solution_2


# SOLUTIONS
print("Part One : " + str(solution_1) + "\nPart Two : " + str(solution_2))
