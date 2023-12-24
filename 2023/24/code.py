# Advent of code Year 2023 Day 24 solution
# Author = brauni
# Date = 2023-12-24
"https://adventofcode.com/2023/day/24"

import re
from collections import Counter
import copy
import os
import math
import numpy as np
import itertools

solution_1, solution_2 = 0, 0

# with open(os.getcwd() + "/AoC_private/2023/24/input.txt", "r") as f:
with open(os.getcwd() + "/2023/24/example.txt", "r") as f:
    input = f.read()
    input = input.split("\n")
    # input = []
    # for line in f.readlines():
    # input.append(int(line))
    # input = [int(line) for line in f.readlines()]
    # input = [line for line in f.readlines()]


# PART 0
def intersect(a, b):
    ca = np.array(a[0][:-1]).T
    va = np.array(a[1][:-1]).T
    cb = np.array(b[0][:-1]).T
    vb = np.array(b[1][:-1]).T

    x, err, rank = np.linalg.lstsq(np.array([va, -vb]).T, cb - ca)[:3]
    # print(x,err,rank)
    if rank == 2:
        print(va,x,ca)
        return va * x[0] + ca
    else:
        return np.array([-1, -1, -1])


def intersect_xy(a, b):
    ca = np.array(a[0][:-1]).T
    va = np.array(a[1][:-1]).T
    cb = np.array(b[0][:-1]).T
    vb = np.array(b[1][:-1]).T

    x, err, rank = np.linalg.lstsq(np.array([va, -vb]).T, cb - ca)[:3]
    if rank == 2:
        print(va,x,ca)
        return va * x[0] + ca
    else:
        return np.array([-1, -1])


# def intersect_p2(meteroites):
#     for i in range()

print(input)
meteroites = {}
for n, line in enumerate(input):
    position = [int(x) for x in line.split(" @ ")[0].split(", ")]
    velocity = [int(x) for x in line.split(" @ ")[1].split(", ")]
    meteroites[n] = (position, velocity)

area = (7,27)
# area = (200000000000000, 400000000000000)
for i, j in itertools.combinations(meteroites, 2):
    a = meteroites[i]
    b = meteroites[j]
    if a == b:
        continue
    x = intersect_xy(a, b)
    if x[0] >= area[0] and x[0] <= area[1] and x[1] >= area[0] and x[1] <= area[1]:
        # direction a
        if (a[1][0] > 0 and x[0] < a[0][0]) or (a[1][0] < 0 and x[0] > a[0][0]):
            continue
        elif (a[1][1] > 0 and x[1] < a[0][1]) or (a[1][1] < 0 and x[1] > a[0][1]):
            continue
        # direction b
        elif (b[1][0] > 0 and x[0] < b[0][0]) or (b[1][0] < 0 and x[0] > b[0][0]):
            continue
        elif (b[1][1] > 0 and x[1] < b[0][1]) or (b[1][1] < 0 and x[1] > b[0][1]):
            continue
        else:
            print(a, b, x)
            solution_1 += 1


# PART 1


# PART 2


# SOLUTIONS

print("Part One : " + str(solution_1) + "\nPart Two : " + str(solution_2))
