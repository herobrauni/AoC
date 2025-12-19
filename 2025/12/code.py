# Advent of Code Year 2025 Day 12 solution
# Author = brauni
# Date = 2025-12-12

import os

from aocd import submit
from aocd.models import Puzzle

puzzle = Puzzle(year=2025, day=12)


# with open(os.getcwd() + "/2025/12/example.txt", 'r') as f:
with open(os.getcwd() + "/AoC_private/2025/12/input.txt", "r") as f:
    input = f.read()
    input = input.split("\n")
    # input = []
    # for line in f.readlines():
    # input.append(int(line))
    # input = [int(line) for line in f.readlines()]
    # input = [line for line in f.readlines()]

print(input)

shapes = input[:30]
fields = input[30:]

# PART 1
solution_1 = 0

for field in fields:
    tmp = field.split(":")[0]
    area = int(tmp.split("x")[0]) * int(tmp.split("x")[1])
    rectangles = 9 * sum([int(x) for x in field.split(" ")[1:]])
    if area >= rectangles:
        solution_1 += 1

### SOLUTION 1
print("Part One : " + str(solution_1))

submit(solution_1, part="a", day=12, year=2025)
