# Advent of Code Year 2024 Day 13 solution
# Author = brauni
# Date = 2024-12-13

import sympy as sym
import re
import os
from aocd import submit
from aocd.models import Puzzle
puzzle = Puzzle(year=2024, day=13)

# with open(os.getcwd() + "/2024/13/example.txt", 'r') as f:
with open(os.getcwd() + "/AoC_private/2024/13/input.txt", 'r') as f:
    input = f.read()
    input = input.split("\n\n")


def sss(a, b, target, p2=False):
    x, y = sym.symbols('x,y')
    eq1 = sym.Eq(int(a[0]) * x + int(b[0]) * y, int(target[0]))
    eq2 = sym.Eq(int(a[1]) * x + int(b[1]) * y, int(target[1]))
    result = sym.solve([eq1, eq2], (x, y))
    if result[x] % 1 == 0 and result[y] % 1 == 0:
        return int(result[x]*3 + result[y])
    else:
        return 0


# # PART 1
solution_1 = 0

for i in input:
    a, b = re.findall(r'Button [A|B]: X\+(\d+), Y\+(\d+)', i)
    target = re.findall(r'Prize: X=(\d+), Y=(\d+)', i)[0]
    solution_1 += sss(a, b, target)


# # SOLUTION 1
print("Part One : " + str(solution_1))

submit(solution_1, part="a", day=13, year=2024)
# PART 2
solution_2 = 0

for i in input:
    # i = input[0]
    a, b = re.findall(r'Button [A|B]: X\+(\d+), Y\+(\d+)', i)
    target = re.findall(r'Prize: X=(\d+), Y=(\d+)', i)[0]
    solution_2 += sss(a, b, target, p2=True)


# SOLUTION 2
print("Part Two : " + str(solution_2))

submit(solution_2, part="b", day=13, year=2024)
