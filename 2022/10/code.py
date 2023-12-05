# Advent of code Year 2022 Day 10 solution
# Author = brauni
# Date = 2022-12-10
"https://adventofcode.com/2022/day/10"

import re
from collections import Counter
import copy
import os
import math

solution_1, solution_2 = 0, 0

# with open(os.getcwd() + "/2022/10/example.txt", 'r') as f:
with open(os.getcwd() + "/AoC_private/2022/10/input.txt", "r") as f:
    input = f.read()
    input = input.split("\n")
    # input = []
    # for line in f.readlines():
    # input.append(int(line))
    # input = [int(line) for line in f.readlines()]
    # input = [line for line in f.readlines()]

# PART 0


print(input)


# PART 1
x = 1
bla = {}
cycle = 0
for row in range(0, len(input)):
    bla[cycle] = x
    if input[row] == "noop":
        cycle += 1
    else:
        bla[cycle + 1] = x
        x = x + int(input[row].split()[1])
        cycle += 2
solution_1 = sum([bla[y - 1] * y for y in range(20, 240, 40)])

# PART 2
for j in range(0, 240):
    i = j if j < 40 else j % 40
    # print(i, bla[i])
    if (i + 1) % 40 == 0:
        print("#") if bla[j] in [i - 1, i, i + 1] else print(" ")
    else:
        print("#", end="") if bla[j] in [i - 1, i, i + 1] else print(" ", end="")

# SOLUTIONS

print("Part One : " + str(solution_1) + "\nPart Two : " + str(solution_2))
