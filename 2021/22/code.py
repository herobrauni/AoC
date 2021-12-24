# Advent of code Year 2021 Day 22 solution
# Author = brauni
# Date = 2021-12-22
"https://adventofcode.com/2021/day/22"

import re
from collections import Counter
import copy
import os
import math
import itertools

solution_1, solution_2 = 0, 0

with open(os.getcwd() + "/2021/22/example.txt", 'r') as f:
    # with open(os.getcwd() + "/2021/22/input.txt", 'r') as f:
    # input = f.read()
    # input = input.split("\n")
    # input = []
    # for line in f.readlines():
    # input.append(int(line))
    # input = [int(line) for line in f.readlines()]
    input = [line.strip() for line in f.readlines()]

# PART 0

"""
print(input)
"""

# PART 1
on = set([])

for line in input[:1]:
    line = line.split(" ")
    mode = line[0]
    x = [int(x) for x in re.findall("-?\d+", line[1].split(",")[0])]
    y = [int(x) for x in re.findall("-?\d+", line[1].split(",")[1])]
    z = [int(x) for x in re.findall("-?\d+", line[1].split(",")[2])]
    if x[0] < -50 or x[1] > 50 or y[0] < -50 or y[1] > 50 or z[0] < -50 or z[1] > 50:
        continue
    products = set(itertools.product(range(int(x[0]), int(x[1]) + 1), range(
        int(y[0]), int(y[1]) + 1), range(int(z[0]), int(z[1]) + 1)))
    print(mode, len(products))
    if mode == "on":
        on = on.union(products)
    elif mode == "off":
        on = on - products

len(on)
# PART 2
line = "on x=-57795..-6158,y=29564..72030,z=20435..90618"


# SOLUTIONS

print("Part One : " + str(solution_1) + "\nPart Two : " + str(solution_2))


x = [0, 1]
y = [0, 4]
z = [0, 3]
set(itertools.product((int(x[0]), int(x[1]) + 1), (
    int(y[0]), int(y[1]) + 1), (int(z[0]), int(z[1]) + 1)))
