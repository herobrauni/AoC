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

# with open(os.getcwd() + "/2021/19/example.txt", 'r') as f:
with open(os.getcwd() + "/2021/19/input.txt", 'r') as f:
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


def do_it(array0, arrayX, vectors_0):
    # array0, arrayX = s[0], s[1]
    combs_directions = list(itertools.product([1, -1], repeat=3))
    # combs_directions = [[-1, 1, 1], [1, -1, 1], [1, 1, -1], [1, 1, 1]]
    comb_columns = list(itertools.permutations(range(0, 3), 3))
    combs_vector = list(itertools.permutations(range(0, max(len(array0), len(arrayX))), 2))

    if np.array_equal(array0, arrayX):
        return None, None, None, 0

    # print(len(array0), len(arrayX))
    orientation = []
    temp, v0 = [], []
    for comb_v in combs_vector:
        v0.append(array0[comb_v[0]] - array0[comb_v[1]])
    for comb_v in combs_vector:
        temp.append(arrayX[comb_v[0]] - arrayX[comb_v[1]])
    temp = np.array(temp)
    v0 = np.array(v0)
    v0_list = v0.tolist()
    all_variations = []
    for comb_c in comb_columns:
        sx = temp[:, [comb_c[0], comb_c[1], comb_c[2]]]
        for comb_d in combs_directions:
            ssx = sx * [comb_d[0], comb_d[1], comb_d[2]]
            all_variations.append(ssx)
            orientation.append([comb_c, comb_d])
    hits = []
    for variation in all_variations:
        hits.append(sum([1 for x in variation if x.tolist() in v0_list]))
    best_variation = all_variations[hits.index(max(hits))]
    best_orientation = orientation[hits.index(max(hits))]

    # Map locations
    p2p = []
    for var in best_variation.tolist():
        if var in v0_list:
            p2p.append((combs_vector[best_variation.tolist().index(var)][0], combs_vector[v0_list.index(var)][1]))
    p2p = list(dict.fromkeys(p2p))
    if len(p2p) < 12:
        # print("failed")
        return None, None, None,  0
    else:
        test_dict = {}
        for x in p2p:
            if x[0] not in test_dict:
                test_dict[x[0]] = [x[1]]
            else:
                test_dict[x[0]] = [test_dict[x[0]], x[1]]
        if any(len(x) > 1 for x in test_dict.values()):
            # print("failed")
            return None, None, None,  0
    # print(p2p)
    # len(p2p)
    # find scanner location
    arrayX = arrayX[:, [best_orientation[0][0], best_orientation[0][1], best_orientation[0][2]]]
    scanner = array0[p2p[0][1]] + (arrayX[p2p[0][0]] * best_orientation[1])
    new_arrayX = []
    for points in arrayX:
        new_arrayX.append(scanner - points*best_orientation[1])
    crosses = []
    for points in p2p:
        crosses.append(array0[points[1]])
    crosses = np.array(crosses)
    # return overlaps
    new_arrayX = [x for x in new_arrayX if sum(x) in range(-10000, 10000)]
    new_arrayX = np.array(new_arrayX)
    return scanner, new_arrayX, crosses, len(p2p)


all_crosses = []
scanners = []
first_run = True
fixed_arrays = []
remaining_arrays = s[:]
test = copy.deepcopy(s[7])
# c = Counter()
# for i in range(len(remaining_arrays)):
#     for j in range(len(remaining_arrays)):
#         print(i, j)
#         scanner, new_arrayX, crosses, len_crosses = do_it(remaining_arrays[i], remaining_arrays[j])
#         if scanner is not None:
#             c[i] += 1
#             print("great success")

i = 0
while len(remaining_arrays) > 0:
    print(i)
    scanner, new_arrayX, crosses, len_crosses = do_it(test, remaining_arrays[i])
    if scanner is not None:
        test = np.append(test, new_arrayX, axis=0)
        test = np.unique(test, axis=0)
        del remaining_arrays[i]
        print("great success")
        i = 0
    else:
        i += 1
len(test)

# c.most_common()

combs_vector = list(itertools.combinations(range(0, max(len(test), len(s[0]))), 2))
len(combs_vector)
