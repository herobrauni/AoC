# Advent of Code Year 2024 Day 2 solution
# Author = brauni
# Date = 2024-12-02

import copy
import re
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


def issafe(line):
    c = 0
    bla = True if x[0] < x[1] else False
    for z in range(1, len(x)):
        if x[z-1] == x[z]:
            return False
        elif abs(x[z-1] - x[z]) > 3:
            return False
        elif x[z-1] < x[z] and bla == True:
            c += 1
        elif x[z-1] > x[z] and bla != True:
            c += 1
        else:
            return False
        # print(c)
    if c == len(x)-1:
        # solution_1 += 1
        return True
    else:
        return False


# PART 1
solution_1 = 0
for line in input:
    x = [int(y) for y in line.split()]
    # print(line)
    solution_1 += 1 if issafe(line) == True else 0


# PART 2
solution_2 = 0
for line in input:
    x = [int(y) for y in line.split()]
    if issafe(line) == True:
        solution_2 += 1
        continue
    for y in range(len(x)):
        og = copy.deepcopy(x)
        x.pop(y)
        if issafe(line) == True:
            solution_2 += 1
            break
        else:
            x = copy.deepcopy(og)


# SOLUTIONS

print("Part One : " + str(solution_1))

submit(solution_1, part="a", day=2, year=2024)


print("Part Two : " + str(solution_2))

submit(solution_2, part="b", day=2, year=2024)
