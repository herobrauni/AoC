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


def do_it(array0, arrayX):
    # array0, arrayX = s[0], s[1]
    combs_directions = list(itertools.product([1, -1], repeat=3))
    comb_columns = list(itertools.permutations(range(0, 3), 3))
    combs_vector_0 = list(itertools.permutations(
        range(0, len(array0)), 2))
    combs_vector_X = list(itertools.permutations(
        range(0, len(arrayX)), 2))

    print(len(combs_vector_0), len(combs_vector_X))
    c = 3
    temp, v0 = [], []
    for comb_v in combs_vector_0:
        v0.append(array0[comb_v[0]] - array0[comb_v[1]])
    for comb_v in combs_vector_X:
        temp.append(arrayX[comb_v[0]] - arrayX[comb_v[1]])
    temp = np.array(temp)
    v0 = np.array(v0)
    v0_list = v0.tolist()
    for comb_c in comb_columns:
        sx = temp[:, [comb_c[0], comb_c[1], comb_c[2]]]
        for comb_d in combs_directions:
            i = 0
            ssx = sx * [comb_d[0], comb_d[1], comb_d[2]]
            ssx_list = ssx.tolist()
            for x in ssx_list:
                if x in v0_list:
                    i += 1
            if i >= c:
                print(i)
                c = i
                fail = 0
                point_to_point = {}
                for i in range(len(ssx_list)):
                    if ssx_list[i] in v0_list:
                        if combs_vector_X[i][0] not in point_to_point:
                            point_to_point[combs_vector_X[i][0]] = combs_vector_0[v0_list.index(ssx_list[i])][0]
                        else:
                            if point_to_point[combs_vector_X[i][0]] != combs_vector_0[v0_list.index(ssx_list[i])][0]:
                                fail += 1
                print(fail)
                if fail == 0:
                    tbr = ssx_list
                    orientation = [comb_c, comb_d]
    if len(point_to_point) == 0:
        return array0
    first = list(point_to_point.keys())[0]
    adv_list = array0.tolist()

    point_pairings = {}
    arrayX_relative = copy.deepcopy(arrayX)
    for i in range(len(arrayX)):
        if i in point_to_point.keys():
            global solution_1
            solution_1 += 1
            point_pairings[str(arrayX[i])] = str(array0[point_to_point[i]])
            arrayX_relative[i] = array0[point_to_point[i]]
    for i in range(len(arrayX)):
        if i not in point_to_point.keys():
            arrayX_relative[i] = array0[point_to_point[first]] + tbr[combs_vector_0.index((first, i))]
            adv_list.append(array0[point_to_point[first]] + tbr[combs_vector_0.index((first, i))])
    print((arrayX[first]*[orientation[1][0], orientation[1][1], orientation[1][2]]), array0[point_to_point[first]])
    sensor = array0[point_to_point[first]] - (arrayX[first]*[orientation[1][0], orientation[1][1], orientation[1][2]])
    adv_list = np.array(adv_list)
    array0 = adv_list
    return arrayX_relative, point_pairings, orientation, sensor


lol, xd, ori, sen = do_it(s[0], s[1])

p = copy.deepcopy(s)
p[1] = lol

lol, xd, ori, sen = do_it(p[1], s[4])
