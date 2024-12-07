# Advent of Code Year 2024 Day 7 solution
# Author = brauni
# Date = 2024-12-07

from multiprocessing import Pool
import itertools
import os
from aocd import submit
from aocd.models import Puzzle
puzzle = Puzzle(year=2024, day=7)

# with open(os.getcwd() + "/2024/07/example.txt", 'r') as f:
with open(os.getcwd() + "/AoC_private/2024/07/input.txt", 'r') as f:
    input = f.read()
    input = input.split("\n")

# print(input)


def solve(line):
    # operators = ["+", "*", "|"]
    e = int(line.split(":")[0])
    z = line.split(" ")[1:]
    z = [int(x) for x in z]
    o = itertools.product(operators, repeat=len(z)-1)
    for x in o:
        u = int(z[0])
        for i, j in enumerate(x):
            if j == "|":
                u = int("".join([str(u), str(z[i+1])]))
            elif j == "+":
                u += z[i+1]
            elif j == "*":
                u *= z[i+1]
        if int(u) == e:
            # print(e)
            return e
    return 0


# PART 1
solution_1 = 0
operators = ["+", "*"]
pool = Pool()
solution_1 = sum(pool.map(solve, input))


# SOLUTION 1
print("Part One : " + str(solution_1))

submit(solution_1, part="a", day=7, year=2024)


# PART 2
solution_2 = 0
operators = ["+", "*", "|"]
pool = Pool()
solution_2 = sum(pool.map(solve, input))

# SOLUTION 2
print("Part Two : " + str(solution_2))

submit(solution_2, part="b", day=7, year=2024)
