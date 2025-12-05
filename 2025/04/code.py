# Advent of Code Year 2025 Day 4 solution
# Author = brauni
# Date = 2025-12-04

import re
import os
import copy
from aocd import submit
from aocd.models import Puzzle
puzzle = Puzzle(year=2025, day=4)


# with open(os.getcwd() + "/2025/04/example.txt", 'r') as f:
with open(os.getcwd() + "/AoC_private/2025/04/input.txt", 'r') as f:
    input = f.read()
    input = input.split("\n")
    # input = []
    # for line in f.readlines():
    # input.append(int(line))
    # input = [int(line) for line in f.readlines()]
    # input = [line for line in f.readlines()]

# print(input)

grid = set()

for i in range(len(input)):
    for j in range(len(input[i])):
        if input[i][j] == '@':
            grid.add(complex(i,j))
# print(grid)

# PART 1
solution_1 = 0

directions = [1, -1, 1j, -1j, 1+1j, 1-1j, -1+1j, -1-1j]
for p in grid:
    c = 0
    for d in directions:
        if p + d in grid:
            c += 1
    if c < 4:
        solution_1 += 1


### SOLUTION 1
print("Part One : " + str(solution_1))

submit(solution_1, part="a", day=4, year=2025)



# PART 2
solution_2 = 0
grid2 = copy.deepcopy(grid)

while True:
    grid = copy.deepcopy(grid2)
    moved = False
    for p in grid:
        c = 0
        for d in directions:
            if p + d in grid:
                c += 1
        if c < 4:
            grid2.remove(p)
            solution_2 += 1
            moved = True
    # print(solution_2)
    if moved == False:
        break


### SOLUTION 2
print("Part Two : " + str(solution_2))

submit(solution_2, part="b", day=4, year=2025)
