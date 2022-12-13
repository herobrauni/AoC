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
import itertools as it
import numpy as np
from datetime import datetime
startTime = datetime.now()


solution_1, solution_2 = 0, 0

# with open(os.getcwd() + "/2021/19/example3.txt", 'r') as f:
with open(os.getcwd() + "/2021/19/input.txt", 'r') as f:
    input = f.read()
    input = input.split("\n\n")

input_formated = []
for line in input:
    line = line.split("\n")
    line = [[int(y) for y in x.split(",")] for x in line if x.find("scanner") == -1]
    input_formated.append(line)
input = copy.deepcopy(input_formated)
print(input)


def distance(a, b):
    return (np.linalg.norm(np.array(a)-np.array(b)))


def distance_vector(a, b):
    return np.array(a)-np.array(b)


def scalar(a, b):
    return np.dot(np.array(a), np.array(b))


def manhattan(a, b):
    return sum(abs(val1-val2) for val1, val2 in zip(a, b))


def variations(vector, n):
    ups = np.array([1, 1, 1]), np.array([1, 1, -1]), np.array([1, -1, 1]), np.array([1, -1, -1]
                                                                                    ), np.array([-1, 1, 1]), np.array([-1, 1, -1]), np.array([-1, -1, 1]), np.array([-1, -1, -1])
    orientations = list(itertools.permutations(vector, 3))
    for i in range(len(orientations)):
        orientations[i] = np.array(orientations[i])
    all_24 = []
    for b in orientations:
        for u in ups:
            all_24.append(np.array(u*b))
    return all_24[n]


def ab2(vecs_0, dt, n, combs_dt):
    inp = list((variations(z, n) for z in dt))
    # combs = list(itertools.combinations(range(len(x)), 2))
    vect_dt = [distance_vector(inp[x[0]], inp[x[1]]) for x in combs_dt]

    dict_overlap = {}
    for i in range(len(vecs_0)):
        for j in range(len(vect_dt)):
            if np.array_equal(vecs_0[i], vect_dt[j]):
                dict_overlap[i] = j
    return dict_overlap


def find_orientation(a, b):
    combs_a = list(itertools.combinations(range(len(a)), 2))
    combs_b = list(itertools.combinations(range(len(b)), 2))
    dist_a = [distance(a[x[0]], a[x[1]]) for x in combs_a]
    dist_b = [distance(b[x[0]], b[x[1]]) for x in combs_b]
    vecs_a = [distance_vector(a[x[0]], a[x[1]]) for x in combs_a]
    dist_overlap = {}
    for i in range(len(dist_a)):
        for j in range(len(dist_b)):
            if dist_a[i] == dist_b[j]:
                dist_overlap[i] = j
    dist_translate = []
    for keys in dist_overlap:
        dist_translate.append((combs_a[keys][0], combs_b[dist_overlap[keys]][0]))
        dist_translate.append((combs_a[keys][1], combs_b[dist_overlap[keys]][1]))
    dist_translate = list(set(dist_translate))
    needed_keys_a = [x[0] for x in dist_translate]
    needed_keys_a = set(needed_keys_a)
    needed_keys_b = [x[1] for x in dist_translate]
    needed_keys_b = set(needed_keys_b)
    a_reduced = [a[x] for x in range(len(a)) if x in needed_keys_a]
    b_reduced = [b[x] for x in range(len(b)) if x in needed_keys_b]
    # print(f"a_red: {len(a_reduced)} / b_red: {len(b_reduced)}")
    vecs_a_reduced = [distance_vector(a_reduced[x[0]], a_reduced[x[1]])
                      for x in list(itertools.combinations(range(len(a_reduced)), 2))]

    test = []
    for n in range(48):
        temp = ab2(vecs_a_reduced, b_reduced, n, list(itertools.combinations(range(len(b_reduced)), 2)))
        c0 = list(itertools.combinations(range(len(a_reduced)), 2))
        c1 = list(itertools.combinations(range(len(b_reduced)), 2))
        # if len(temp) > test[1]:
        if len(temp) > 0:
            temp_translate = []
            for keys in temp:
                temp_translate.append((c0[int(keys)][0], c1[temp[keys]][0]))
                temp_translate.append((c0[int(keys)][1], c1[temp[keys]][1]))
            fuckthisdict = {}
            for x in temp_translate:
                if x[0] not in list(fuckthisdict.keys()):
                    fuckthisdict[x[0]] = set([])
                fuckthisdict[x[0]].add(x[1])
            if sum([1 if len(fuckthisdict[x]) > 1 else 0 for x in fuckthisdict]) == 0 and len(fuckthisdict) > 2:
                dict_overlap = ab2(vecs_a, b, n, combs_b)
                translate = []
                for keys in dict_overlap:
                    translate.append((combs_df[keys][0], combs_dt[dict_overlap[keys]][0]))
                    translate.append((combs_df[keys][1], combs_dt[dict_overlap[keys]][1]))
                translate = list(set(translate))
                test.append([n, len(temp), translate])
    return test


dfin, dtodo = {}, {}

dfin['0'] = [np.array(x) for x in input[0]]
for i in range(1, len(input)):
    dtodo[str(i)] = input[i]

tested_combs = set([])
hitmarker = []
scanners = {}
scanners['0'] = np.array([0, 0, 0])
lb = 66
skip = set([])

while len(dfin) < len(input):
    dfin_temp = copy.deepcopy(dfin)
    for df in dfin:
        combs_df = list(itertools.combinations(range(len(dfin[df])), 2))
        dist_df = [distance(dfin[df][x[0]], dfin[df][x[1]]) for x in combs_df]
        vect_df = [distance_vector(dfin[df][x[0]], dfin[df][x[1]]) for x in combs_df]
        for dt in dtodo:
            if dt in list(dfin_temp.keys()):
                continue
            if (int(df), int(dt)) in skip:
                continue
            if int(df) == int(dt):
                continue
            combs_dt = list(itertools.combinations(range(len(dtodo[dt])), 2))
            dist_dt = [distance(dtodo[dt][x[0]], dtodo[dt][x[1]])
                       for x in combs_dt]
            if sum([1 for x in dist_dt if x in dist_df]) < lb:
                continue
            fo = find_orientation(dfin[df], dtodo[dt])
            if len(fo) > 1:
                print("Error")
                break
            n = fo[0][0]
            translate = fo[0][2]
            if len(translate) > 0:
                print(f"HIT {dt}<->{df} on Variation {n} of Sensor {dt}")
                temp_inp = [variations(y, n) for y in dtodo[dt]]
                temp_scanner = np.array(dfin[df][translate[0][0]]) - temp_inp[translate[0][1]]
                scanners[dt] = temp_scanner
                temp_inp = [y + temp_scanner for y in temp_inp]
                dfin_temp[dt] = temp_inp
                print("")
                break
    dfin = copy.deepcopy(dfin_temp)

input_finished = set([])
for df in dfin:
    for b in dfin[df]:
        input_finished.add(tuple(b))
solution_1 = len(input_finished)

print(datetime.now() - startTime)


for i in scanners:
    for j in scanners:
        md = manhattan(scanners[i], scanners[j])
        if md > solution_2:
            solution_2 = md

print(datetime.now() - startTime)

print("Part One : " + str(solution_1) + "\nPart Two : " + str(solution_2))
