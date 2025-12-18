# Advent of Code Year 2025 Day 10 solution
# Author = brauni
# Date = 2025-12-10

import os

import numpy as np
from aocd import submit
from aocd.models import Puzzle
from scipy.optimize import Bounds, LinearConstraint, milp

puzzle = Puzzle(year=2025, day=10)


# with open(os.getcwd() + "/2025/10/example.txt", "r") as f:
with open(os.getcwd() + "/AoC_private/2025/10/input.txt", "r") as f:
    input = f.read()
    input = input.split("\n")
    # input = []
    # for line in f.readlines():
    # input.append(int(line))
    # input = [int(line) for line in f.readlines()]
    # input = [line for line in f.readlines()]


# PART 2
solution_2 = 0

# print(input)
inp = []
for line in input:
    tmp = line.split(" ")
    joltage = eval(tmp[-1].replace("{", "[").replace("}", "]"))
    buttons = [eval(x) for x in tmp[1:-1]]
    buttons_count = []
    for btn in buttons:
        tmp = [0] * len(joltage)
        if isinstance(btn, tuple):
            for idx in btn:
                tmp[idx] = 1
        else:
            tmp[btn] = 1
        buttons_count.append(tmp)

    inp.append([buttons_count, joltage])

bounds = Bounds(lb=0, ub=np.inf)

for line in inp:
    print(line)
    costs = np.array([1] * len(line[0]))
    tmp = np.array(line[0])
    np_buttons = tmp.transpose()
    goal = np.array(line[1])
    constraints = LinearConstraint(np_buttons, goal, goal)
    integrality = np.ones_like(costs)
    res = milp(c=costs, constraints=constraints, integrality=integrality, bounds=bounds)
    print(int(res.fun))
    solution_2 += int(res.fun)


### SOLUTION 2
print("Part Two : " + str(solution_2))

submit(solution_2, part="b", day=10, year=2025)
