# Advent of code Year 2015 Day 12 solution
# Author = brauni
# Date = 2023-11-17
"https://adventofcode.com/2015/day/12"

import json
import re
from collections import Counter
import copy
import os
import math

solution_1, solution_2 = 0, 0

# with open(os.getcwd() + "/2015/12/example.txt", "r") as f:
with open(os.getcwd() + "/2015/12/input.txt", "r") as f:
    input = f.read()

# PART 0
print(input)

# PART 1
solution_1 = sum([int(x) for x in re.findall(r"-?\d+", input)])

# PART 2
table = json.loads(input)


def value_without_red(x):
    if type(x) == int:
        return x
    elif type(x) == list:
        return sum([value_without_red(y) for y in x])
    elif type(x) == dict:
        if "red" in x.values():
            return 0
        else:
            return value_without_red(list(x.values()))
    return 0


solution_2 = value_without_red(table)


# SOLUTIONS
print("Part One : " + str(solution_1) + "\nPart Two : " + str(solution_2))
