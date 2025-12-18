# Advent of Code Year 2024 Day 11 solution
# Author = brauni
# Date = 2024-12-11


import copy
import math
import os
from collections import Counter
from aocd import submit
from aocd.models import Puzzle
puzzle = Puzzle(year=2024, day=11)

# with open(os.getcwd() + "/2024/11/example.txt", 'r') as f:
with open(os.getcwd() + "/AoC_private/2024/11/input.txt", 'r') as f:
    input = f.read()

print(input)


def blink(n, g):
    for i in range(n):
        f = Counter()
        for x in g:
            if x == 0:
                f[1] += g[x]
            # faster way to calculate length (in digits) of int
            elif (int(math.log10(x))+1) % 2 == 0:
                xx = str(x)
                t1, t2 = int(xx[:len(xx)//2]), int(xx[len(xx)//2:])
                f[t1] += g[x]
                f[t2] += g[x]
            else:
                f[x*2024] += g[x]
        g = copy.deepcopy(f)
    return g


# PART 1
g = Counter([int(x) for x in input.split()])
solution_1 = sum(blink(25, g).values())

# SOLUTION 1
print("Part One : " + str(solution_1))

submit(solution_1, part="a", day=11, year=2024)


# PART 2
solution_2 = sum(blink(75, g).values())

# # SOLUTION 2
print("Part Two : " + str(solution_2))

submit(solution_2, part="b", day=11, year=2024)
