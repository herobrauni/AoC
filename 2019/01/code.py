# Advent of Code Year 2019 Day 1 solution
# Author = brauni
# Date = 2019-12-01

import re
import os
from aocd import submit
from aocd.models import Puzzle
puzzle = Puzzle(year=2019, day=1)


# with open(os.getcwd() + "/2019/01/example.txt", 'r') as f:
with open(os.getcwd() + "/2019/01/input.txt", 'r') as f:
    # input = f.read()
    # input = input.split("\n")
    # input = []
    # for line in f.readlines():
    # input.append(int(line))
    # input = [int(line) for line in f.readlines()]
    input = [line for line in f.readlines()]

"""
print(input)
"""


# PART 1


# PART 2


# SOLUTIONS

print("Part One : " + str(solution_1))

"""
submit("10", part="a", day=1, year=2019)
"""

print("Part Two : " + str(solution_2))

"""
submit(solution_2, part="b", day=1, year=2019)
"""
