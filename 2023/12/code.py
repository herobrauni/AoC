# Advent of code Year 2023 Day 12 solution
# Author = brauni
# Date = 2023-12-12
"https://adventofcode.com/2023/day/12"

import re
from collections import Counter
import copy
import os
import math
import itertools
from functools import cache

solution_1, solution_2 = 0, 0

with open(os.getcwd() + "/AoC_private/2023/12/input.txt", "r") as f:
# with open(os.getcwd() + "/2023/12/example.txt", "r") as f:
    input = f.read()
    input = input.split("\n")


# PART 0
print(input)

@cache
def solve(g, n, gears, numbers, r=0):
    if g == len(gears):
        return n == len(numbers)

    if gears[g] in ".?":
        r += solve(g + 1, n, gears, numbers)

    try:
        q = g + numbers[n]
        if gears[g] in "#?" and "." not in gears[g:q] and "#" not in gears[q]:
            r += solve(q + 1, n + 1, gears, numbers)
    except IndexError:
        pass

    return r

# PART 1
for line in input:
    gears, numbers = line.split()
    gears = gears + "?"
    numbers = tuple([int(x) for x in numbers.split(",")])
    solution_1 += solve(0, 0, gears, numbers)

# PART 2
for line in input:
    gears, numbers = line.split()
    gears = (gears + "?") *5
    numbers = tuple([int(x) for x in numbers.split(",")]*5)
    solution_2 += solve(0, 0, gears, numbers)

# SOLUTIONS

print("Part One : " + str(solution_1) + "\nPart Two : " + str(solution_2))
