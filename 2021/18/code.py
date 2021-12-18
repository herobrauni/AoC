# Advent of code Year 2021 Day 18 solution
# Author = brauni
# Date = 2021-12-18
"https://adventofcode.com/2021/day/18"

import re
from collections import Counter
import copy
import os
import math
import ast


solution_1, solution_2 = 0, 0

with open(os.getcwd() + "\\2021\\18\\example.txt", 'r') as f:
    # with open(os.getcwd() + "\\2021\\18\\input.txt", 'r') as f:
    # input = f.read()
    # input = input.split("\n")
    # input = []
    # for line in f.readlines():
    # input.append(int(line))
    # input = [int(line) for line in f.readlines()]
    input = [line for line in f.readlines()]

# PART 0
test = ast.literal_eval(input[0])
# if not isinstance(test, int):
#     for a in range(len(test)):
#         if not isinstance(test[a], int):
#             for b in range(len(test[a])):
#                 if not isinstance(test[a][b], int):
#                     for c in range(len(test[a][b])):
#                         if not isinstance(test[a][b][c], int):
#                             for d in range(len(test[a][b][c])):
#                                 print(test[a][b][c][d])


def depth(l):
    if isinstance(l, list):
        return 1 + max(depth(item) for item in l)
    else:
        return 0


def levels(l, depth=-1):
    if not isinstance(l, list):
        yield (l, depth)
    else:
        for sublist in l:
            yield from levels(sublist, depth + 1)


def flatten(container):
    for i in container:
        if isinstance(i, (list, tuple)):
            for j in flatten(i):
                yield j
        else:
            yield i


list(levels(test))

deepest_elements = [x for x in list(levels(test)) if x[1] == depth(test)-1]
left_deepest_element = [x[0] for x in deepest_elements[:2]]

in_string = input[0]
flat = list(flatten(test))

if (str(flat).rfind(str(left_deepest_element[0])+", "+str(left_deepest_element[1]))) - 3 > 0:
    left_from_deep = int(str(flat)[(str(flat).rfind(
        str(left_deepest_element[0])+", "+str(left_deepest_element[1]))) - 3])

if (str(flat).rfind(str(left_deepest_element[0])+", "+str(left_deepest_element[1]))) - 3 

in_string.replace(str(left_deepest_element).replace(" ", ""), "X")
"""
print(input)
"""
# PART 1


# PART 2


# SOLUTIONS

# print("Part One : " + str(solution_1) + "\nPart Two : " + str(solution_2))
