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
import numpy as np
from scipy.spatial import ConvexHull


solution_1, solution_2 = 0, 0

with open(os.getcwd() + "/2021/22/example.txt", "r") as f:
    # with open(os.getcwd() + "/AoC_private/2021/22/input.txt", 'r') as f:
    input = [line.strip() for line in f.readlines()]

input_formated = []

for line in input:
    line = line.split(" ")
    mode = line[0]
    x = [int(x) for x in re.findall("-?\d+", line[1].split(",")[0])]
    y = [int(x) for x in re.findall("-?\d+", line[1].split(",")[1])]
    z = [int(x) for x in re.findall("-?\d+", line[1].split(",")[2])]
    input_formated.append([x, y, z, mode])

# PART 0
"""
print(input)
"""
x_on = set()
y_on = set()
z_on = set()


# PART 1
for line in input_formated:
    # if line[0][0] < -50 or line[0][1] > 50 or line[1][0] < -50 or line[1][1] > 50 or line[2][0] < -50 or line[2][1] > 50:
    #     continue
    if line[3] == "on":
        x_on.update(set(range(line[0][0], line[0][1] + 1)))
        y_on.update(set(range(line[1][0], line[1][1] + 1)))
        z_on.update(set(range(line[2][0], line[2][1] + 1)))
    elif line[3] == "off":
        # x_on.difference_update(set(range(line[0][0], line[0][1]+1)))
        # y_on.difference_update(set(range(line[1][0], line[1][1]+1)))
        # z_on.difference_update(set(range(line[2][0], line[2][1]+1)))
        x_on = x_on - set(range(line[0][0], line[0][1] + 1))
        y_on = y_on - set(range(line[1][0], line[1][1] + 1))
        z_on = z_on - set(range(line[2][0], line[2][1] + 1))
    # print(x_on, y_on, z_on)


len(x_on) * len(y_on) * len(z_on)
# len(z_on)


# set([1, 2, 3, 4, 5]).difference(set([1, 2, 3]))
