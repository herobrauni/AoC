# Advent of code Year 2023 Day 12 solution
# Author = brauni
# Date = 2023-12-12
"https://adventofcode.com/2023/day/12"

import re
from collections import Counter
import copy
import os
import math
import itertools

solution_1, solution_2 = 0, 0

# with open(os.getcwd() + "/AoC_private/2023/12/input.txt", "r") as f:
with open(os.getcwd() + "/2023/12/example.txt", "r") as f:
    input = f.read()
    input = input.split("\n")
    # input = []
    # for line in f.readlines():
    # input.append(int(line))
    # input = [int(line) for line in f.readlines()]
    # input = [line for line in f.readlines()]

# PART 0


print(input)


def isvalid(gears, numbers):
    g = re.findall(r"#+", gears)
    if len(re.findall(r"#", gears)) != sum([int(x) for x in numbers.split(",")]):
        return False
    for n, number in enumerate([int(x) for x in numbers.split(",")]):
        if len(g[n]) != number:
            return False
    else:
        return True


def combos(gears):
    l = len(re.findall(r"\?", gears))
    cs = []
    it = list(set(itertools.product([".", "#"], repeat=l)))
    for y in it:
        tmp = list(gears)
        finds = [x.start() for x in re.finditer(r"\?", gears)]
        for n, f in enumerate(finds):
            tmp[f] = y[n]
        cs.append("".join(tmp))
    return cs


# PART 1
for line in input:
    gears, numbers = line.split()
    gs = combos(gears)
    for g in gs:
        if isvalid(g, numbers):
            print(g)
            solution_1 += 1


# gears = "????.######..#####."
# re.findall(r"(?=([\?|\.]*[\?|#]{1}[\?|\.]+[\?|#]{1}[\?|\.]+[\?|#]{3}[\?|\.]*))",gears)

x = 1
# print(pattern)
# # PART 2
for line in input:
    for i in range(3):
        gears = (line.split()[0] + "?") * i + line.split()[0]
        numbers = (line.split()[1] + ",") * i + line.split()[1]
        pattern = "(?=([\?|\.]*"
        for x in [int(x) for x in numbers.split(",")]:
            pattern += f"[\?|\.]*[\?|#]{ {x} }"
        pattern += "[\?|\.]*))"
        print(pattern)
        print(gears)
    # gs = combos(gears)
#     for g in gs:
#         if isvalid(g, numbers):
#             solution_2 += 1
print(pattern)

# SOLUTIONS

print("Part One : " + str(solution_1) + "\nPart Two : " + str(solution_2))
