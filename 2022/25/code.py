# Advent of code Year 2022 Day 25 solution
# Author = brauni
# Date = 2022-12-27
"https://adventofcode.com/2022/day/25"

import re
from collections import Counter
import copy
import os
import math
import itertools

solution_1, solution_2 = 0, 0

# with open(os.getcwd() + "/2022/25/example.txt", 'r') as f:
with open(os.getcwd() + "/AoC_private/2022/25/input.txt", "r") as f:
    input = f.read()
    input = input.split("\n")
    # input = []
    # for line in f.readlines():
    # input.append(int(line))
    # input = [int(line) for line in f.readlines()]
    # input = [line for line in f.readlines()]


# PART 0
def trans_numbers(a):
    total = 0
    a = a[::-1]
    for i in range(len(a)):
        match a[i]:
            case "2":
                x = 2
            case "1":
                x = 1
            case "0":
                x = 0
            case "-":
                x = -1
            case "=":
                x = -2
        total = total + x * (5**i)
    return total


def trans_numbers_rev(solution_1):
    abc = []
    for i in range(0, 100, 1):
        x = 5**i
        abc.append([2 * x, 1 * x, 0, -1 * x, -2 * x])

    bla = []
    numbers = []
    i = 0
    while True:
        if solution_1 in range(
            sum([x[4] for x in abc[0:i]]), sum([x[0] for x in abc[0:i]]) + 1
        ):
            break
        i += 1

    s = solution_1
    i -= 1
    for i in range(i, 0, -1):
        # print(i)
        for j in range(len(abc[i])):
            # if s + abc[i][j] in range(abc[i-1][4],abc[i-1][0]+1):
            if s - abc[i][j] in range(
                sum([x[4] for x in abc[0:i]]), sum([x[0] for x in abc[0:i]]) + 1
            ):
                s = s - abc[i][j]
                numbers.append(abc[i][j])
                bla.append(j)
                # print(abc[i][j], s)
                break

    for i in range(len(abc[0])):
        if s - abc[0][i] == 0:
            numbers.append(abc[0][i])
            bla.append(i)
            break
    trans = ["2", "1", "0", "-", "="]
    return "".join([trans[x] for x in bla])


# PART 1
solution_1_dec = 0
for line in input:
    solution_1_dec = solution_1_dec + trans_numbers(line)

solution_1 = trans_numbers_rev(solution_1_dec)

# SOLUTIONS
print("Part One : " + str(solution_1) + "\nPart Two : " + str(solution_2))
