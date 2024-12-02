# Advent of code Year 2021 Day 8 solution
# Author = brauni
# Date = 2021-12-08
"https://adventofcode.com/2021/day/8"

import re
from collections import Counter
import copy
import os

solution_1, solution_2 = 0, 0

# with open(os.getcwd() + "\\2021\\08\\example.txt", 'r') as f:
with open(os.getcwd() + "\\2021\\08\\input.txt", "r") as f:
    input = [line for line in f.readlines()]

# PART 0
inp, out = [], []
for line in input:
    x = line.split("|")
    inp += [y.strip() for y in x[0].split()]
    out += [y.strip() for y in x[1].split()]


"""
print(input)
"""

# PART 1
count = 0
for line in out:
    if re.match(r"\b[a-g]{2,4}\b|\b[a-g]{7}\b", line):
        count += 1
solution_1 = count


# PART 2
s = 0
for x, y in [x.split("|") for x in input]:  # split signal and output
    l = {len(s): set(s) for s in x.split()}  # get number of segments

    n = ""
    for o in map(set, y.split()):  # loop over output digits
        # print(o)
        match len(o), len(o & l[4]), len(o & l[2]):  # mask with known digits
            case 2, _, _:
                n += "1"
            case 3, _, _:
                n += "7"
            case 4, _, _:
                n += "4"
            case 7, _, _:
                n += "8"
            case 5, 2, _:
                n += "2"
            case 5, 3, 1:
                n += "5"
            case 5, 3, 2:
                n += "3"
            case 6, 4, _:
                n += "9"
            case 6, 3, 1:
                n += "6"
            case 6, 3, 2:
                n += "0"
    # print(n)
    s += int(n)

solution_2 = s


# SOLUTIONS

print("Part One : " + str(solution_1) + "\nPart Two : " + str(solution_2))
