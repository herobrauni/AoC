# Advent of Code Year 2024 Day 2 solution
# Author = brauni
# Date = 2024-12-02

import copy
import os
from aocd import submit
from aocd.models import Puzzle
puzzle = Puzzle(year=2024, day=2)

# with open(os.getcwd() + "/2024/02/example.txt", 'r') as f:
with open(os.getcwd() + "/AoC_private/2024/02/input.txt", 'r') as f:
    input = f.read()
    input = input.split("\n")
    # input = []
    # for line in f.readlines():
    # input.append(int(line))
    # input = [int(line) for line in f.readlines()]
    # input = [line for line in f.readlines()]

print(input)


def issafe(line_list):
    c = 0
    slope = True if line_list[0] < line_list[1] else False
    for z in range(1, len(line_list)):
        if line_list[z-1] == line_list[z]:
            return False
        elif abs(line_list[z-1] - line_list[z]) > 3:
            return False
        elif line_list[z-1] < line_list[z] and slope:
            c += 1
        elif line_list[z-1] > line_list[z] and not slope:
            c += 1
        else:
            return False
    if c == len(line_list)-1:
        return True
    else:
        return False


# PART 1
solution_1 = 0
for line in input:
    line_list = [int(y) for y in line.split()]
    solution_1 += 1 if issafe(line_list) else 0


# PART 2
solution_2 = 0
for line in input:
    line_list = [int(y) for y in line.split()]
    if issafe(line_list):
        solution_2 += 1
        continue
    for y in range(len(line_list)):
        og = copy.deepcopy(line_list)
        line_list.pop(y)
        if issafe(line_list):
            solution_2 += 1
            break
        else:
            line_list = copy.deepcopy(og)


# SOLUTIONS

print("Part One : " + str(solution_1))

submit(solution_1, part="a", day=2, year=2024)


print("Part Two : " + str(solution_2))

submit(solution_2, part="b", day=2, year=2024)
