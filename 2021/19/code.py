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

absolute_pos = {}
for line in input_formated:
    for row in line:
        if "scanner" in str(row):
            scanner = row.replace("scanner", "").replace(
                " ", "").replace("-", "")
            absolute_pos[scanner] = []
        else:
            row = [int(x) for x in row.split(",")]
            absolute_pos[scanner].append(row)


distances = {}
combs = list(itertools.combinations(range(0, len(input_formated[0])-1), 2))
for scanner in absolute_pos:
    for comb in combs:
        name = str("s"+scanner+"-"+str(comb[0])+"|"+str(comb[1]))
        distances[name] = int(sum([(a-b)**2 for a, b in zip(absolute_pos[scanner]
                              [comb[0]], absolute_pos[scanner][comb[1]])])**(1/2))

keys0 = list([x for x in distances.keys() if "s0" in x])
scanner0 = {x: distances[x] for x in keys0}

bla = {}
for s0 in scanner0:
    bla[s0] = [x for x in distances.keys() if "s1" in x and distances[x]
               == distances[s0]]

bla_keys = list(bla.keys())
for line in bla_keys:
    if bla[line] == []:
        del bla[line]


c = {}
for line in bla:
    if line.split("-")[1].split("|")[0] not in c:
        c[line.split("-")[1].split("|")[0]] = Counter()
    if line.split("-")[1].split("|")[1] not in c:
        c[line.split("-")[1].split("|")[1]] = Counter()
    for row in bla[line]:
        c[line.split("-")[1].split("|")[0]
          ] += Counter(row.split("-")[1].split("|")[0])
        c[line.split("-")[1].split("|")[1]
          ] += Counter(row.split("-")[1].split("|")[1])

for line in bla:
    print(line)

for line in c:
    print(line, c[line].most_common(1))