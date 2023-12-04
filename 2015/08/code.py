# Advent of code Year 2015 Day 8 solution
# Author = brauni
# Date = 2023-12-02
"https://adventofcode.com/2015/day/8"

import re
from collections import Counter
import copy
import os
import math
import numpy as np

solution_1, solution_2 = 0, 0

# with open(os.getcwd() + "/2015/08/example.txt", "r") as f:
with open(os.getcwd() + "/2015/08/input.txt", 'r') as f:
    input = f.read()
    input = input.split("\n")
    # input = []
    # for line in f.readlines():
    # input.append(int(line))
    # input = [int(line) for line in f.readlines()]
# input = [line for line in f.readlines()]

# PART 0


print(input)

literals = 0
memory = 0
# PART 1
for line in input:
    z = len(line)
    x = eval(line)
    literals += z
    memory += len(x)

solution_1 = literals - memory
# PART 2
reps = 0
for line in input:
    x = re.findall(r'\\|\"',line)
    y = len(x)+len(line)+2
    reps+=y

solution_2 = reps - literals

# SOLUTIONS
print("Part One : " + str(solution_1) + "\nPart Two : " + str(solution_2))
