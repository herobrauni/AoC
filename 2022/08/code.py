# Advent of code Year 2022 Day 8 solution
# Author = brauni
# Date = 2022-12-08
"https://adventofcode.com/2022/day/8"

import re
from collections import Counter
import copy
import os
import math

solution_1, solution_2 = 0, 0

# with open(os.getcwd() + "/2022/08/example.txt", 'r') as f:
with open(os.getcwd() + "/2022/08/input.txt", 'r') as f:
    input = f.read()
    input = input.split("\n")
    input = [list(x) for x in input]
    # input = []
    # for line in f.readlines():
    # input.append(int(line))
    # input = [int(line) for line in f.readlines()]
    # input = [line for line in f.readlines()]

# PART 0
for i in range(0, len(input)):
    for j in range(0, len(input[i])):
        input[i][j] = int(input[i][j])

print(input)

# PART 1
for i in range(0, len(input)):
    for j in range(0, len(input[i])):
        input[i][j] = int(input[i][j])
        if i == 0 or j == 0 or i == len(input)-1 or j == len(input[i])-1:
            # print(input[i][j])
            solution_1 += 1
            continue
        elif input[i][j] > max([x[j] for x in input[:i]]):  # upwards
            # print(input[i], input[i][j])
            solution_1 += 1
            continue
        elif input[i][j] > max([x[j] for x in input[i+1:]]):  # downwards
            # print(input[i], input[i][j])
            solution_1 += 1
            continue
        elif input[i][j] > max(input[i][:j]):  # left
            # print(input[i], input[i][j])
            solution_1 += 1
            continue
        elif input[i][j] > max(input[i][j+1:]):  # right
            # print(input[i], input[i][j])
            solution_1 += 1
            continue

# PART 2
ss = []
for i in range(0, len(input)):
    for j in range(0, len(input[i])):
        if i == 0 or j == 0 or i == len(input)-1 or j == len(input[i])-1:
            # print(input[i][j])
            continue
        upwards = [x[j] for x in input[:i]]
        temp = 0
        for y in range(len(upwards), 0, -1):
            if upwards[y-1] < input[i][j]:
                temp += 1
            else:
                temp += 1
                break
        ss.append(temp)
        left = input[i][:j]
        temp = 0
        for y in range(len(left), 0, -1):
            if left[y-1] < input[i][j]:
                temp += 1
            else:
                temp += 1
                break
        ss.append(temp)
        downwards = [x[j] for x in input[i+1:]]
        temp = 0
        for y in range(0, len(downwards), 1):
            if downwards[y] < input[i][j]:
                temp += 1
            else:
                temp += 1
                break
        ss.append(temp)
        right = input[i][j+1:]
        temp = 0
        for y in range(0, len(right), 1):
            if right[y] < input[i][j]:
                temp += 1
            else:
                temp += 1
                break
        ss.append(temp)

        if solution_2 < math.prod(ss):
            solution_2 = math.prod(ss)
        ss = []

# SOLUTIONS

print("Part One : " + str(solution_1) + "\nPart Two : " + str(solution_2))
