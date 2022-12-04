# Advent of code Year 2022 Day 4 solution
# Author = brauni
# Date = 2022-12-04
"https://adventofcode.com/2022/day/4"

import re
from collections import Counter
import copy
import os
import math

solution_1, solution_2 = 0, 0

# with open(os.getcwd() + "/2022/04/example.txt", 'r') as f:
with open(os.getcwd() + "/2022/04/input.txt", 'r') as f:
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
for line in input:
    a = line.split(",")[0].split("-")
    b = line.split(',')[1].split("-")
    if (int(a[0]) >= int(b[0]) and int(a[1]) <= int(b[1])) or (int(b[0]) >= int(a[0]) and int(b[1]) <= int(a[1])):
        # print(a, b)
        solution_1 += 1


# PART 2
for line in input:
    a = line.split(",")[0].split("-")
    a = [int(x) for x in a]
    b = line.split(',')[1].split("-")
    b = [int(x) for x in b]
    if a[0] in range(b[0],
                     b[1] + 1) or a[1] in range(b[0],
                                                b[1] + 1) or b[0] in range(a[0],
                                                                           a[1] + 1) or b[1] in range(a[0],
                                                                                                      a[1] + 1):
        # print(a, b)
        solution_2 += 1


# SOLUTIONS

print("Part One : " + str(solution_1) + "\nPart Two : " + str(solution_2))
