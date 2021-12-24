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

with open(os.getcwd() + "/2021/22/example.txt", 'r') as f:
    # with open(os.getcwd() + "/2021/22/input.txt", 'r') as f:
    input = [line.strip() for line in f.readlines()]

# PART 0

"""
print(input)
"""

# PART 1
on = []
off = []


def calc_overlap(a, b):
    if len(a) == 3:
        i = 0
    elif len(a) == 4:
        i = 1
    x1 = a[i]
    x2 = b[i]
    y1 = a[i+1]
    y2 = b[i+1]
    z1 = a[i+2]
    z2 = b[i+2]
    # overlap_x = [min([x for x in range(x1[0], x1[1] + 1)
    #                  if x in range(x2[0], x2[1] + 1)]), max([x for x in range(x1[0], x1[1] + 1)
    #                                                          if x in range(x2[0], x2[1] + 1)])]
    o_x = set(range(x1[0], x1[1]+1)).intersection(set(range(x2[0], x2[1]+1)))
    if len(o_x) == 0:
        overlap_x = [0, 0]
    else:
        overlap_x = [min(o_x), max(o_x)]
    o_y = set(range(y1[0], y1[1]+1)).intersection(set(range(y2[0], y2[1]+1)))
    if len(o_y) == 0:
        overlap_y = [0, 0]
    else:
        overlap_y = [min(o_y), max(o_y)]
    o_z = set(range(z1[0], z1[1]+1)).intersection(set(range(z2[0], z2[1]+1)))
    if len(o_z) == 0:
        overlap_z = [0, 0]
    else:
        overlap_z = [min(o_z), max(o_z)]
    return [overlap_x, overlap_y, overlap_z]


def calc_volume(a):
    if len(a) == 3:
        i = 0
    elif len(a) == 4:
        i = 1
    x1 = a[i]
    y1 = a[i+1]
    z1 = a[i+2]
    volume = (x1[1] - x1[0] + 1) * (y1[1] - y1[0] + 1) * (z1[1] - z1[0] + 1)
    return volume


def non_overlap_value(a, b):
    return calc_volume(a) + calc_volume(b) - calc_volume(calc_overlap(a, b))


def is_overlap(a, b):
    return True if calc_overlap(a, b) != [[0, 0], [0, 0], [0, 0]] else False


off_value, on_value = 0, 0

for line in input:
    line = line.split(" ")
    mode = line[0]
    x = [int(x) for x in re.findall("-?\d+", line[1].split(",")[0])]
    y = [int(x) for x in re.findall("-?\d+", line[1].split(",")[1])]
    z = [int(x) for x in re.findall("-?\d+", line[1].split(",")[2])]
    if x[0] < -50 or x[1] > 50 or y[0] < -50 or y[1] > 50 or z[0] < -50 or z[1] > 50:
        continue
    volume_temp = 0
    if mode == "on":
        for b in on:
            off.append(calc_overlap([x, y, z], b))
            volume_temp += calc_volume(calc_overlap([x, y, z], b))
        on.append([x, y, z])
        on_value += calc_volume([x, y, z])
        off_value += volume_temp if volume_temp < calc_volume(
            [x, y, z]) else calc_volume([x, y, z])
        # print(calc_volume([x, y, z]))
    elif mode == "off":
        for b in on:
            off.append(calc_overlap([x, y, z], b))
            off_value += calc_volume(calc_overlap([x, y, z], b))
            # print(calc_volume([x, y, z]))
    print(f"on: {on_value} off: {off_value} diff: {on_value - off_value}")


is_overlap([[0, 0], [0, 0], [0, 0]], [[1, 10], [1, 10], [1, 10]])
