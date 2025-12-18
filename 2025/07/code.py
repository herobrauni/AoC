# Advent of Code Year 2025 Day 7 solution
# Author = brauni
# Date = 2025-12-07

import os
from aocd import submit
from aocd.models import Puzzle
puzzle = Puzzle(year=2025, day=7)


# with open(os.getcwd() + "/2025/07/example.txt", 'r') as f:
with open(os.getcwd() + "/AoC_private/2025/07/input.txt", 'r') as f:
    input = f.read()
    input = input.split("\n")
    # input = []
    # for line in f.readlines():
    # input.append(int(line))
    # input = [int(line) for line in f.readlines()]
    # input = [line for line in f.readlines()]

print(input)

grid = set()

for i in range(len(input)):
    for j in range(len(input[i])):
        if input[i][j] == '^':
            grid.add(complex(i,j))
        elif input[i][j] == "S":
            start = complex(i,j)

# PART 1
solution_1 = 0


def p1(grid, pos, sol):
    for i in range(int(pos.real), len(input)):
        current = complex(i, pos.imag)
        if current in sol:
            return sol
        if current in grid:
            sol.add(current)
            return sol.union(p1(grid, complex(i, pos.imag + 1), sol),
                           p1(grid, complex(i, pos.imag - 1), sol))
    return sol

solution_1 = len(p1(grid,start,set()))

### SOLUTION 1
print("Part One : " + str(solution_1))

submit(solution_1, part="a", day=7, year=2025)

# PART 2
solution_2 = 0

memo = {}

def p2(grid, pos):
    if pos in memo:
        return memo[pos]
    
    for i in range(int(pos.real), len(input)):
        current = complex(i, pos.imag)
        if current in grid:
            memo[pos] = p2(grid, complex(i, pos.imag - 1)) + p2(grid, complex(i, pos.imag + 1))
            return memo[pos]
    
    memo[pos] = 1
    return 1

solution_2 = p2(grid, start)

### SOLUTION 2
print("Part Two : " + str(solution_2))

submit(solution_2, part="b", day=7, year=2025)
