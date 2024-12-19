# Advent of Code Year 2024 Day 19 solution
# Author = brauni
# Date = 2024-12-19

import re
import os
from aocd import submit
from aocd.models import Puzzle
puzzle = Puzzle(year=2024, day=19)

# with open(os.getcwd() + "/2024/19/example.txt", 'r') as f:
with open(os.getcwd() + "/AoC_private/2024/19/input.txt", 'r') as f:
    input = f.read()
    input = input.split("\n\n")

print(input)
towels = input[0].split(", ")
designs = input[1].split("\n")


def check(design, towels, memo=None):
    if memo is None:
        memo = {}
    if design in memo:
        return memo[design]
    if design == "":
        return 1

    total_count = 0
    for towel in towels:
        if design.startswith(towel):
            rest = design[len(towel):]
            c_towel = check(rest, towels, memo)
            total_count += c_towel
    memo[design] = total_count
    return total_count


# PART 1 / 2
solution_1 = 0
solution_2 = 0

for design in designs:
    if t := check(design, towels):
        solution_1 += 1
        solution_2 += t

# SOLUTION 1
print("Part One : " + str(solution_1))

submit(solution_1, part="a", day=19, year=2024)

# SOLUTION 2
print("Part Two : " + str(solution_2))

submit(solution_2, part="b", day=19, year=2024)
