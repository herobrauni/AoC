# Advent of code Year 2022 Day 2 solution
# Author = brauni
# Date = 2022-12-02
"https://adventofcode.com/2022/day/2"

import re
from collections import Counter
import copy
import os
import math

solution_1, solution_2 = 0, 0

# with open(os.getcwd() + "/2022/02/example.txt", 'r') as f:
with open(os.getcwd() + "/AoC_private/2022/02/input2.txt", "r") as f:
    input = f.read()
    input = input.split("\n")
    # input = []
    # for line in f.readlines():
    # input.append(int(line))
    # input = [int(line) for line in f.readlines()]
    # input = [line for line in f.readlines()]

# PART 0

# """
# print(input)
# """

# PART 1
for line in input:
    if line[0] == "A":
        if line[2] == "X":
            solution_1 += 1 + 3
        if line[2] == "Y":
            solution_1 += 2 + 6
        if line[2] == "Z":
            solution_1 += 3 + 0
    if line[0] == "B":
        if line[2] == "X":
            solution_1 += 1 + 0
        if line[2] == "Y":
            solution_1 += 2 + 3
        if line[2] == "Z":
            solution_1 += 3 + 6
    if line[0] == "C":
        if line[2] == "X":
            solution_1 += 1 + 6
        if line[2] == "Y":
            solution_1 += 2 + 0
        if line[2] == "Z":
            solution_1 += 3 + 3
    print(solution_1)

# PART 2

# X Lose
# Y Draw
# Z Win

for line in input:
    if line[0] == "A":  # Rock
        if line[2] == "X":
            solution_2 += 3 + 0
        if line[2] == "Y":
            solution_2 += 1 + 3
        if line[2] == "Z":
            solution_2 += 2 + 6
    if line[0] == "B":  # Paper
        if line[2] == "X":
            solution_2 += 1 + 0
        if line[2] == "Y":
            solution_2 += 2 + 3
        if line[2] == "Z":
            solution_2 += 3 + 6
    if line[0] == "C":  # Scissors
        if line[2] == "X":
            solution_2 += 2 + 0
        if line[2] == "Y":
            solution_2 += 3 + 3
        if line[2] == "Z":
            solution_2 += 1 + 6

# SOLUTIONS

print("Part One : " + str(solution_1) + "\nPart Two : " + str(solution_2))
