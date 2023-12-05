# Advent of code Year 2015 Day 7 solution
# Author = brauni
# Date = 2023-11-17
"https://adventofcode.com/2015/day/7"

import re
from collections import Counter
import copy
import os
import math
import ctypes

solution_1, solution_2 = 0, 0

# with open(os.getcwd() + "/2015/07/example.txt", "r") as f:
with open(os.getcwd() + "/AoC_private/2015/07/input.txt", "r") as f:
    input = f.read()
    input = input.split("\n")
    # input = []
    # for line in f.readlines():
    # input.append(int(line))
    # input = [int(line) for line in f.readlines()]
    # input = [line for line in f.readlines()]


# PART 0
print(input)


def rec(x):
    if x.isdigit():
        return x
    line = blub[x]
    # print(line, x)
    if str(line).isdigit():
        return int(line)
    elif re.search("AND", line):
        return int(rec(line.split()[0])) & int(rec(line.split()[2]))
    elif re.search("OR", line):
        return int(rec(line.split()[0])) | int(rec(line.split()[2]))
    elif re.search("NOT", line):
        return ctypes.c_uint16(~int(rec(line.split()[1]))).value
    elif re.search("LSHIFT", line):
        return int(rec(line.split()[0])) * 2 ** int(line.split()[2])
    elif re.search("RSHIFT", line):
        return int(rec(line.split()[0])) // 2 ** int(line.split()[2])
    else:
        return rec(line)


# PART 1
blub = {}

for line in input:
    x = line.split(" -> ")[1]
    blub[x] = line.split(" -> ")[0]


for key in sorted(blub.keys()):
    if key != "a":
        # print(key)
        blub[key] = rec(key)

# for i in blub:
#     print(i, blub[i])

# blub["a"]
solution_1 = rec("a")


# PART 2
blub = {}

for line in input:
    x = line.split(" -> ")[1]
    blub[x] = line.split(" -> ")[0]

blub["b"] = solution_1

for key in sorted(blub.keys()):
    if key != "a":
        # print(key)
        blub[key] = rec(key)

solution_2 = rec("a")
# SOLUTIONS

print("Part One : " + str(solution_1) + "\nPart Two : " + str(solution_2))
