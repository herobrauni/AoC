# Advent of code Year 2021 Day 9 solution
# Author = brauni
# Date = 2021-12-09
"https://adventofcode.com/2021/day/9"

import re
from collections import Counter
import copy
import os
import math

solution_1, solution_2 = 0, 0

# with open(os.getcwd() + "\\2021\\09\\example.txt", 'r') as f:
with open(os.getcwd() + "\\2021\\09\\input.txt", "r") as f:
    input = f.read()
    input = input.split("\n")

# PART 0
inp = []
for line in input:
    inp.append(list(map(int, str(line))))
# Create a Border of 9s around the array to prevent out of bounds errors
# We start at 1,1 to avoid the border, imagine an old school snake field
input = copy.deepcopy(inp)
for line in input:
    line.insert(0, 9)
    line.append(9)
border = [9] * len(input[0])
input.insert(0, border)
input.append(border)

"""
print(input)
"""

# PART 1

lowpoints = []

# iterate through all points and check if the current point is smaller than ALL the neighbours
# we start at +1 and end at -1 to avoid the border
for i in range(1, len(input) - 1):
    for j in range(1, len(input[0]) - 1):
        if input[i][j] < min(
            input[i - 1][j], input[i + 1][j], input[i][j - 1], input[i][j + 1]
        ):
            lowpoints.append(input[i][j])

solution_1 = sum([x + 1 for x in lowpoints])


# PART 2
# Test if a given point is 9 and return 0 if it is
# otherwise set it to 9 (to prevent repetition) and recursively check the neighbours
def check_neighbours(inp, i, j):
    if inp[i][j] == 9:
        return 0
    else:
        inp[i][j] = 9
    return (
        1
        + check_neighbours(inp, i - 1, j)
        + check_neighbours(inp, i + 1, j)
        + check_neighbours(inp, i, j - 1)
        + check_neighbours(inp, i, j + 1)
    )


clusters = []
# iterate through all points and check the size of the basin it belongs to, if any
for i in range(1, len(input) - 1):
    for j in range(1, len(input[0]) - 1):
        clusters.append(check_neighbours(input, i, j))

clusters.sort(reverse=True)

solution_2 = math.prod(clusters[:3])

# SOLUTIONS

print("Part One : " + str(solution_1) + "\nPart Two : " + str(solution_2))
