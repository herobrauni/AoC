# Advent of code Year 2015 Day 17 solution
# Author = brauni
# Date = 2023-12-18
"https://adventofcode.com/2015/day/17"

import re
from collections import Counter
import copy
import os
import math
import itertools

solution_1, solution_2 = 0, 0

with open(os.getcwd() + "/AoC_private/2015/17/input.txt", "r") as f:
# with open(os.getcwd() + "/2015/17/example.txt", 'r') as f:
    # input = f.read()
    # input = input.split("\n")
    # input = []
    # for line in f.readlines():
    # input.append(int(line))
    input = [int(line) for line in f.readlines()]
    # input = [line for line in f.readlines()]

# PART 0


print(input)


# PART 1
goal = 150

cl = {}

for i in range(len(input)):
    bla = itertools.combinations(input, i)
    for x in bla:
        if sum(x) == goal:
            solution_1 += 1
            if len(x) in cl.keys():
                cl[len(x)] +=1
            else:
                cl[len(x)] = 1

cl = sorted(cl.items())
# PART 2


# SOLUTIONS
solution_2 = cl[0][1]
print("Part One : " + str(solution_1) + "\nPart Two : " + str(solution_2))
