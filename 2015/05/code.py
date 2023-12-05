# Advent of code Year 2015 Day 5 solution
# Author = brauni
# Date = 2023-11-17
"https://adventofcode.com/2015/day/5"

import re
from collections import Counter
import copy
import os
import math

solution_1, solution_2 = 0, 0

# with open(os.getcwd() + "/2015/05/example.txt", "r") as f:
with open(os.getcwd() + "/2015/05/input.txt", "r") as f:
    input = f.read()
    input = input.split("\n")
    # input = []
    # for line in f.readlines():
    # input.append(int(line))
    # input = [int(line) for line in f.readlines()]
    # input = [line for line in f.readlines()]

# PART 0


print(input)


# PART 1
for x in input:
    for nope in ["ab", "cd", "pq", "xy"]:
        if nope in x:
            # print(x)
            break
    else:
        if (
            len(re.findall("a|e|i|o|u", str(x))) >= 3
            and len(re.findall("(.)\\1{1,}", x)) > 0
        ):
            solution_1 += 1


# PART 2
for x in input:
    if len(re.findall("(..).*\\1", x)) > 0 and len(re.findall("(.).\\1", x)) > 0:
        solution_2 += 1

# SOLUTIONS

print("Part One : " + str(solution_1) + "\nPart Two : " + str(solution_2))
