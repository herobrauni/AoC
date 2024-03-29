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

# PART 0

"""
print(input)
"""

# PART 1


def calc_overlap(a, b):
    x1, y1, z1 = a[0], a[1], a[2]
    x2, y2, z2 = b[0], b[1], b[2]
    o_x = set(range(x1[0], x1[1] + 1)).intersection(set(range(x2[0], x2[1] + 1)))
    if len(o_x) == 0:
        overlap_x = [0, 0]
    else:
        overlap_x = [min(o_x), max(o_x)]
    o_y = set(range(y1[0], y1[1] + 1)).intersection(set(range(y2[0], y2[1] + 1)))
    if len(o_y) == 0:
        overlap_y = [0, 0]
    else:
        overlap_y = [min(o_y), max(o_y)]
    o_z = set(range(z1[0], z1[1] + 1)).intersection(set(range(z2[0], z2[1] + 1)))
    if len(o_z) == 0:
        overlap_z = [0, 0]
    else:
        overlap_z = [min(o_z), max(o_z)]
    return [overlap_x, overlap_y, overlap_z]


def non_overlap_value(a, b):
    return calc_volume(a) + calc_volume(b) - calc_volume(calc_overlap(a, b))


def overlap_value(a, b):
    return calc_volume(calc_overlap(a, b))


def is_overlap(a, b):
    return True if calc_overlap(a, b) != [[0, 0], [0, 0], [0, 0]] else False


def generate_corners(a):
    return list(
        itertools.product(
            (int(x[0]), int(x[1]) + 1),
            (int(y[0]), int(y[1]) + 1),
            (int(z[0]), int(z[1]) + 1),
        )
    )


on, off = [], []

x_on = []

on_val, off_val = 0, 0
i = 0
test = []
first_run_on, first_run_off = True, True
for line in input:
    line = line.split(" ")
    mode = line[0]
    x = [int(x) for x in re.findall("-?\d+", line[1].split(",")[0])]
    y = [int(x) for x in re.findall("-?\d+", line[1].split(",")[1])]
    z = [int(x) for x in re.findall("-?\d+", line[1].split(",")[2])]
    # if x[0] < -50 or x[1] > 50 or y[0] < -50 or y[1] > 50 or z[0] < -50 or z[1] > 50:
    #     continue
    # print(x, y, z)
    if mode == "on":
        for b in on:
            if is_overlap(b, [x, y, z]):
                print("overlap")
        on.append([x, y, z])
