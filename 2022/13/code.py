# Advent of code Year 2022 Day 13 solution
# Author = brauni
# Date = 2022-12-13
"https://adventofcode.com/2022/day/13"

import re
from collections import Counter
import copy
import os
import math
import numpy as np
import itertools

solution_1, solution_2 = 0, 0

# with open(os.getcwd() + "/2022/13/example.txt", 'r') as f:
with open(os.getcwd() + "/2022/13/input.txt", 'r') as f:
    input = f.read()
    input = input.split("\n\n")
    # input = []
    # for line in f.readlines():
    # input.append(int(line))
    # input = [int(line) for line in f.readlines()]
    # input = [line for line in f.readlines()]
    input = [x.split("\n") for x in input]


# PART 0

input_p1 = copy.deepcopy(input)
for i in range(len(input)):
    for j in range(len(input[i])):
        input_p1[i][j] = eval(input[i][j])


def compare(a, b):
    # print(a, b)
    if isinstance(a, int) and isinstance(b, int) and a < b:
        return True
    elif isinstance(a, int) and isinstance(b, int) and a > b:
        return False
    elif isinstance(a, int) and isinstance(b, int) and a == b:
        return
    elif isinstance(a, list) and isinstance(b, list):
        if len(a) < len(b):  # a smaller
            for i in range(len(a)):
                z = compare(a[i], b[i])
                if z is True:
                    return True
                elif z is False:
                    return False
            return True
        elif len(a) > len(b):  # b smaller
            for i in range(len(b)):
                z = compare(a[i], b[i])
                if z is True:
                    return True
                elif z is False:
                    return False
            return False
        else:
            for i in range(len(b)):
                z = compare(a[i], b[i])
                if z is True:
                    return True
                elif z is False:
                    return False
    elif not isinstance(a, type(b)):
        a = [a] if isinstance(a, int) else a
        b = [b] if isinstance(b, int) else b
        return compare(a, b)


# PART 1
t = [[]]*len(input_p1)
for i in range(len(input_p1)):
    t[i] = compare(input_p1[i][0], input_p1[i][1])
    print(t[i])

solution_1 = sum([x+1 for x in range(len(t)) if t[x] == True])

# PART 2
dividers = [[[2]], [[6]]]

input_p2 = []
for i in range(len(input)):
    for j in range(len(input[i])):
        input_p2.append(eval(input[i][j]))

input_p2.append([[2]])
input_p2.append([[6]])

temp_dir = {}
while temp_dir != input_p2:
    temp_dir = copy.deepcopy(input_p2)
    for i in range(len(input_p2)-1):
        if compare(input_p2[i], input_p2[i+1]) is False:
            t1, t2 = input_p2[i], input_p2[i+1]
            input_p2[i], input_p2[i+1] = t2, t1

solution_2 = math.prod([x+1 for x in range(len(input_p2)) if input_p2[x] in dividers])

# SOLUTIONS

print("Part One : " + str(solution_1) + "\nPart Two : " + str(solution_2))
