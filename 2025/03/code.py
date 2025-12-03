# Advent of Code Year 2025 Day 3 solution
# Author = brauni
# Date = 2025-12-03

import re
import os
from aocd import submit
from aocd.models import Puzzle
puzzle = Puzzle(year=2025, day=3)


with open(os.getcwd() + "/2025/03/example.txt", 'r') as f:
# with open(os.getcwd() + "/AoC_private/2025/03/input.txt", 'r') as f:
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

for line in input:
    a = [bla for bla in line[:-1]]
    amax = max(a)
    for i in range(len(line)):
        if line[i] == amax:
            break
    b = [bla for bla in line[i+1:]]
    bmax = max(b)
    print(int(amax+bmax))
    solution_1 += int(amax+bmax)


### SOLUTION 1
print("Part One : " + str(solution_1))

submit(solution_1, part="a", day=3, year=2025)

# PART 2
solution_2 = 0

for line in input:
    tmp = []
    todo = len(line) -12

    for i in line:
        while todo > 0 and tmp and i > tmp[-1]:
            tmp.pop()
            todo -= 1
        tmp.append(i)
        print(tmp)
    if todo > 0:
        tmp = tmp[:-todo]
    sol = ''.join(tmp)
    print(sol)
    solution_2 += int(sol)

### SOLUTION 2
print("Part Two : " + str(solution_2))

submit(solution_2, part="b", day=3, year=2025)
