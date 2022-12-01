# Advent of code Year 2021 Day 19 solution
# Author = brauni
# Date = 2021-12-21
"https://adventofcode.com/2021/day/19"

import re
from collections import Counter
import copy
import os
import math
import itertools
import numpy as np

solution_1, solution_2 = 0, 0

with open(os.getcwd() + "/2021/19/example.txt", 'r') as f:
    # with open(os.getcwd() + "/2021/19/input.txt", 'r') as f:
    input = f.read()
    input = input.split("\n\n")
    # input = []
    # for line in f.readlines():
    # input.append(int(line))
    # input = [int(line) for line in f.readlines()]
    # input = [line for line in f.readlines()]

# PART 0
input_formated = []
for line in input:
    line = line.split("\n")
    input_formated.append(line)

s = []
i = 0
for scanner in input_formated:
    temp = []
    s.append([])
    for points in scanner[1:]:
        points = [int(x) for x in points.split(",")]
        temp.append(points)
    s[i] = np.array(temp)
    i += 1

combs_vector = list(itertools.permutations(
    range(0, len(input_formated[0])-1), 2))

vectors0 = []
for comb_v in combs_vector:
    vectors0.append(s[0][comb_v[0]] - s[0][comb_v[1]])
vectors0 = np.array(vectors0)
v0 = set([",".join([str(x[0]), str(x[1]), str(x[2])]) for x in vectors0])

vd_0 = {}
for comb_v in combs_vector:
    vd_0[str(s[0][comb_v[0]] - s[0][comb_v[1]])] = comb_v

vectors1 = []
for comb_v in combs_vector:
    vectors1.append(s[1][comb_v[0]] - s[1][comb_v[1]])
vectors1 = np.array(vectors1)


def return_oriented_vectors(vectors0, vectors1):
    combs = list(itertools.product([1, -1], repeat=3))
    comb_columns = list(itertools.permutations(range(0, 3), 3))
    combs_vector = list(itertools.permutations(
        range(0, len(input_formated[0])-1), 2))
    v0 = set([",".join([str(x[0]), str(x[1]), str(x[2])]) for x in vectors0])
    vt = 0
    for comb_c in comb_columns:
        sx = vectors1
        sx = sx[:, [comb_c[0], comb_c[1], comb_c[2]]]
        for comb in combs:
            ssx = sx * [comb[0], comb[1], comb[2]]
            ssx = np.array(ssx)
            v1 = set([",".join([str(x[0]), str(x[1]), str(x[2])])
                      for x in ssx])
            if len(v1.intersection(v0)) > 0:
                print(len(v1.intersection(v0)))
                vx = v1.intersection(v0)
                if len(vx) > vt:
                    vt = len(vx)
                    dx = {}
                    for comb_v in combs_vector:
                        dx[str(ssx[comb_v[0]] - ssx[comb_v[1]])] = comb_v
                        # dx[comb_v] = (ssx[comb_v[0]] - ssx[comb_v[1]])
    return dx


v1_dict = return_oriented_vectors(vectors0, vectors1)

str(v1_dict[(0, 1)])

vd_0[str(v1_dict[(0, 1)])]

new_coordinates = {}

for vector in v1_dict:
    if vector in vd_0.keys():
        print(v1_dict[vector][0], vd_0[vector][0])
        new_coordinates[v1_dict[vector][0]] = vd_0[vector][0]
        # maps the x array point to the 0 array point
first = list(new_coordinates.keys())[0]
for i in range(len(s[1])):
    if i in new_coordinates.keys():
        s[1][i] = s[0][new_coordinates[i]]
for i in range(len(s[1])):
    if i not in new_coordinates.keys():
        s[1][i] = s[1][first] + v1_dict[(first, i)]


len(new_coordinates)

for x in new_coordinates:
    # print(x)
    print(s[0][new_coordinates[x]], s[1][x])


print(s[0][9])
# list(new_coordinates.keys())[0]

len(set(dict.fromkeys(list(v1_dict.keys()))).intersection(
    set(dict.fromkeys(list(vd_0.keys())))))
set(dict.fromkeys(list(vd_0.keys())))
