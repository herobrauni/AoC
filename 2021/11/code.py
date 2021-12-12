# Advent of code Year 2021 Day 11 solution
# Author = brauni
# Date = 2021-12-11
"https://adventofcode.com/2021/day/11"

import re
from collections import Counter
import copy
import os
import math

solution_1, solution_2 = 0, 0

# with open(os.getcwd() + "\\2021\\11\\example.txt", 'r') as f:
with open(os.getcwd() + "\\2021\\11\\input.txt", 'r') as f:
    input = f.read()
    input = input.split("\n")


# PART 0
inp = []
for line in input:
    inp.append(list(map(int, str(line))))

input = copy.deepcopy(inp)
"""
print(input)
"""

# PART 1
for line in input:
    line.insert(0, "X")
    line.append("X")
border = ["X"] * len(input[0])
input.insert(0, border)
input.append(border)

for line in input:
    print(line)


# Recursive function to check if a number is 9, if it is add 1 to all neighbours
# Otherwise add 1 to the number
# Skip over the X's and F's (X is the border, F is already flashed)
def cn(inp, x, y):
    # print(x, y, inp[x][y])
    if inp[x][y] == "X" or inp[x][y] == "F":
        return 0
    if inp[x][y] >= 9:
        inp[x][y] = "F"
        return 1 + cn(inp, x - 1, y) + cn(inp, x + 1, y) + cn(inp, x, y - 1) + cn(inp, x, y + 1) + cn(inp, x - 1, y - 1) + cn(inp, x + 1, y + 1) + cn(inp, x - 1, y + 1) + cn(inp, x + 1, y - 1)
    else:
        inp[x][y] += 1
        return 0


bla = copy.deepcopy(input)

# Iterate through all numbers in the field (except the border) and run the recursive function for each
# In the end reset all flashed Numbers F to 0
for z in range(100):
    for i in range(1, len(bla) - 1):
        for j in range(1, len(bla[0]) - 1):
            solution_1 += cn(bla, i, j)
    for i in range(1, len(bla) - 1):
        for j in range(1, len(bla[0]) - 1):
            if bla[i][j] == "F":
                bla[i][j] = 0


# PART 2
# How many fields are there that need to flash at the same time?
all_flash = (len(input)-2)*(len(input[0])-2)
bla = copy.deepcopy(input)

# iterate a arbitrary number of times, we stop if we find the first all flashed anyways
# Run the same as in p1 but check if all fields have flashed after every run
# Safe the run on which all fields have flashed as the solution
for z in range(10000):
    test = 0
    for i in range(1, len(bla) - 1):
        for j in range(1, len(bla[0]) - 1):
            test += cn(bla, i, j)
    for i in range(1, len(bla) - 1):
        for j in range(1, len(bla[0]) - 1):
            if bla[i][j] == "F":
                bla[i][j] = 0
    if test == all_flash:
        solution_2 = z + 1
        break

# SOLUTIONS
print("Part One : " + str(solution_1) + "\nPart Two : " + str(solution_2))
