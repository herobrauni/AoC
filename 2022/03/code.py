# Advent of code Year 2022 Day 3 solution
# Author = brauni
# Date = 2022-12-03
"https://adventofcode.com/2022/day/3"

import re
from collections import Counter
import copy
import os
import math

solution_1, solution_2 = 0, 0

# with open(os.getcwd() + "/2022/03/example.txt", 'r') as f:
with open(os.getcwd() + "/AoC_private/2022/03/input.txt", "r") as f:
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
for line in input:
    # line_split[0] =
    first = line[: int(len(line) / 2)]
    second = line[int(len(line) / 2) :]
    bla = ord(list(set(first).intersection(second))[0])
    if bla in range(97, 123):  # lower
        solution_1 += bla - 96
    if bla in range(65, 91):
        solution_1 += bla - 38
# PART 2

for i in range(0, len(input)):
    print(i)
    if (i + 1) % 3 == 0:
        print(i)
        bla = ord(
            list(
                set(set(input[i]).intersection(input[i - 1])).intersection(input[i - 2])
            )[0]
        )
        # SOLUTIONS
        if bla in range(97, 123):  # lower
            solution_2 += bla - 96
        if bla in range(65, 91):
            solution_2 += bla - 38


print("Part One : " + str(solution_1) + "\nPart Two : " + str(solution_2))
