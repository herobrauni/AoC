# Advent of code Year 2015 Day 4 solution
# Author = brauni
# Date = 2023-11-17
"https://adventofcode.com/2015/day/4"

import re
from collections import Counter
import copy
import os
import math
import hashlib

solution_1, solution_2 = 0, 0

# with open(os.getcwd() + "/2015/04/example.txt", "r") as f:
with open(os.getcwd() + "/AoC_private/2015/04/input.txt", "r") as f:
    input = f.read()
    # input = input.split("\n")
    # input = []
    # for line in f.readlines():
    # input.append(int(line))
    # input = [int(line) for line in f.readlines()]
    # input = [line for line in f.readlines()]

# PART 0

# PART 1
c = 1
while True:
    x = input + str(c)
    if hashlib.md5(x.encode()).hexdigest()[:5] == "00000":
        break
    c += 1
solution_1 = c


# PART 2
c = 1
while True:
    x = input + str(c)
    if hashlib.md5(x.encode()).hexdigest()[:6] == "000000":
        break
    c += 1
solution_2 = c


# SOLUTIONS

print("Part One : " + str(solution_1) + "\nPart Two : " + str(solution_2))
