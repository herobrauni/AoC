# Advent of code Year 2023 Day 1 solution
# Author = brauni
# Date = 2023-12-01
"https://adventofcode.com/2023/day/1"

import re
from collections import Counter
import copy
import os
import math
import numpy as np

solution_1, solution_2 = 0, 0

# with open(os.getcwd() + "/2023/01/example.txt", "r") as f:
with open(os.getcwd() + "/AoC_private/2023/01/input.txt", "r") as f:
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
    numbers = re.findall(r'\d', x)
    solution_1 += int(str(numbers[0]) + str(numbers[-1]))


# PART 2
solution_2 = 0
for x in input:
    # need to use "lookahead" to include overlapps
    numbers = re.findall(r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))", x)
    z, t = numbers[0], numbers[-1]
    for i, n in enumerate(
        ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    ):
        if numbers[0] == n:
            z = i + 1
        if numbers[-1] == n:
            t = i + 1

    solution_2 += int(str(z) + str(t))

# SOLUTIONS
print("Part One : " + str(solution_1) + "\nPart Two : " + str(solution_2))
