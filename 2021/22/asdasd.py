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
import matplotlib.pyplot as plt


solution_1, solution_2 = 0, 0

with open(os.getcwd() + "/2021/22/example.txt", "r") as f:
    # with open(os.getcwd() + "/AoC_private/2021/22/input.txt", 'r') as f:
    input = [line.strip() for line in f.readlines()]

# PART 0

"""
print(input)
"""

# PART 1


def find_intersection(x, y):
    if len(range(max(x[0], y[0]), min(x[-1], y[-1]))) == 0:
        return None
    return max(x[0], y[0]), min(x[-1], y[-1])


def find_overlap(a, b):
    x = find_intersection(a[0], b[0])
    # y = find_intersection(a[1], b[1])
    # z = find_intersection(a[2], b[2])
    if x is None:  # or y is None:
        return None
    return [x]  # , y]  # , z]


def calc_volume(a):
    # * (a[2][1] - a[2][0]+1)
    return a[0][1] - a[0][0] + 1  # * (a[1][1] - a[1][0]+1)


def combined_value(l):
    with_overlaps = sum(calc_volume(a) for a in l)
    overlaps = 0
    print(with_overlaps, overlaps)


# bla = []
# a = [[0, 3], [0, 3], "on"]
# b = [[2, 4], [2, 4], "on"]
# c = [[1, 4], [2, 5], "on"]
# bla.append(a)
# bla.append(b)
# bla.append(c)

bla = []
a = [[0, 4], "on"]
b = [[2, 6], "on"]
c = [[1, 8], "on"]
bla.append(a)
bla.append(b)
bla.append(c)


on = []
on_value = 0

for line in bla:
    mode = line[-1]
    coords = line[:-1]
    if mode == "on":
        overlaps = []
        for already_on in on:
            if find_overlap(already_on, coords) is not None:
                print(find_overlap(already_on, coords))
        on.append(coords)

combined_value([a, b, c])
find_overlap(a, b)

bla = []
a = [[0, 4], "on"]  # grün
b = [[2, 612312312], "on"]  # blau
c = [[1, 8], "on"]  # rot
bla.append(a[0])
bla.append(b[0])
bla.append(c[0])


def total_overlap(a):
    overlaps = []
    combs = list(itertools.combinations(a, 2))
    for comb in combs:
        print(comb[1])
        if find_overlap(comb) is not None:
            overlaps.append(find_overlap(comb))
    return overlaps


total_overlap(bla)
