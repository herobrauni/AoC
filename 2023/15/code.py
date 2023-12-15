# Advent of code Year 2023 Day 15 solution
# Author = brauni
# Date = 2023-12-15
"https://adventofcode.com/2023/day/15"

import re
from collections import Counter
import copy
import os
import math

solution_1, solution_2 = 0, 0

with open(os.getcwd() + "/AoC_private/2023/15/input.txt", "r") as f:
    # with open(os.getcwd() + "/2023/15/example.txt", "r") as f:
    input = f.read()
    input = input.split(",")
    # input = []
    # for line in f.readlines():
    # input.append(int(line))
    # input = [int(line) for line in f.readlines()]
    # input = [line for line in f.readlines()]

# PART 0


print(input)


def hash_that(line):
    r = 0
    line = [x for x in line]
    for x in line:
        r += ord(x)
        r = r * 17
        r = r % 256
    return r


# PART 1
for line in input:
    solution_1 += hash_that(line)


# PART 2
test = {}
for i in range(256):
    test[i] = []

for line in input:
    hsh = re.findall(r"[a-z]+", line)[0]
    operation = re.findall(r"[-|=]", line)[0]
    box = hash_that(hsh)

    if operation == "=":
        focal = re.findall(r"\d+", line)[0]
        if hsh not in [x[0] for x in test[box]]:
            test[box].append([hsh, focal])
        else:
            n = [n for n, x in enumerate(test[box]) if x[0] == hsh][0]
            test[box][n] = [hsh, focal]
    else:
        if hsh in [x[0] for x in test[box]]:
            n = [n for n, x in enumerate(test[box]) if x[0] == hsh][0]
            tmp = test[box].pop(n)

for box in test:
    if len(test[box]) == 0:
        continue
    for n, lens in enumerate(test[box]):
        solution_2 += (1 + box) * (n + 1) * int(lens[1])
# SOLUTIONS

print("Part One : " + str(solution_1) + "\nPart Two : " + str(solution_2))
# box = 0
