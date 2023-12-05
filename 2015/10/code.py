# Advent of code Year 2015 Day 10 solution
# Author = brauni
# Date = 2023-11-17
"https://adventofcode.com/2015/day/10"

import re
from collections import Counter
import copy
import os
import math

solution_1, solution_2 = 0, 0

# with open(os.getcwd() + "/2015/10/example.txt", 'r') as f:
with open(os.getcwd() + "/2015/10/input.txt", "r") as f:
    input = f.read()

# PART 0
print(input)

# PART 1 / 2 combined
z = input
for i in range(50):
    test1 = re.finditer(r"(\d)\1*", z)
    z = []
    for test in test1:
        z.append(test.end() - test.start())
        z.append(test.group()[0])
    z = "".join([str(x) for x in z])
    if i == 39:
        solution_1 = len(z)
        print("Part One : " + str(solution_1))
solution_2 = len(z)

# SOLUTIONS
print("Part One : " + str(solution_1) + "\nPart Two : " + str(solution_2))
