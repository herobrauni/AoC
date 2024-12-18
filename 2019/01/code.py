# Advent of Code Year 2019 Day 1 solution
# Author = brauni
# Date = 2019-12-01

import re
import os
from aocd import submit
from aocd.models import Puzzle
puzzle = Puzzle(year=2019, day=1)


# with open(os.getcwd() + "/2019/01/example.txt", 'r') as f:
with open(os.getcwd() + "/AoC_private/2019/01/input.txt", 'r') as f:
    input = f.read()
    input = input.split("\n")
    # input = []
    # for line in f.readlines():
    # input.append(int(line))
    # input = [int(line) for line in f.readlines()]
    # input = [line for line in f.readlines()]

print(input)


# PART 1
solution_1 = 0
for x in input:
    solution_1 += (int(x) // 3) - 2


# PART 2
solution_2 = 0
for x in input:
    y = x
    while True:
        solution_2 += (int(y) // 3 - 2) if (int(y) // 3-2) >= 0 else 0
        x = (int(y) // 3 - 2) if (int(y) // 3-2) >= 0 else 0
        print(x, y)
        y = x

        if y <= 0:
            break

# SOLUTIONS

print("Part One : " + str(solution_1))

submit(solution_1, part="a", day=1, year=2019)

print("Part Two : " + str(solution_2))

submit(solution_2, part="b", day=1, year=2019)
