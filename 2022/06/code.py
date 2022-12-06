# Advent of code Year 2022 Day 6 solution
# Author = brauni
# Date = 2022-12-06
"https://adventofcode.com/2022/day/6"

import re
from collections import Counter
import copy
import os
import math

solution_1, solution_2 = 0, 0

# with open(os.getcwd() + "/2022/06/example.txt", 'r') as f:
with open(os.getcwd() + "/2022/06/input.txt", 'r') as f:
    input = f.read()
    # input = input.split("\n")
    # input = []
    # for line in f.readlines():
    # input.append(int(line))
    # input = [int(line) for line in f.readlines()]
    # input = [line for line in f.readlines()]

# PART 0

print(input)

input = list(input)

# PART 1
for i in range(4, len(input)):
    bla = input[i-4:i]
    bla = list(dict.fromkeys(bla))
    if(len(bla) == 4):
        solution_1 = i
        # print(bla)
        break

# PART 2
for i in range(14, len(input)):
    bla = input[i-14:i]
    bla = list(dict.fromkeys(bla))
    if(len(bla) == 14):
        solution_2 = i
        # print(bla)
        break

# SOLUTIONS

print("Part One : " + str(solution_1) + "\nPart Two : " + str(solution_2))
