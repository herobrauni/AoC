# Advent of Code Year 2025 Day 1 solution
# Author = brauni
# Date = 2025-12-01

import os
from aocd import submit
from aocd.models import Puzzle
puzzle = Puzzle(year=2025, day=1)


# with open(os.getcwd() + "/2025/01/example.txt", 'r') as f:
with open(os.getcwd() + "/AoC_private/2025/01/input.txt", 'r') as f:
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
pos = 50
for move in input:
    direction = move[0]
    distance = int(move[1:])
    if direction == "L":
        pos = pos - distance
    else:
        pos = pos + distance
    pos = pos%100
    print(pos)
    if pos == 0:
        solution_1 = solution_1 + 1

### SOLUTION 1
print("Part One : " + str(solution_1))

submit(solution_1, part="a", day=1, year=2025)



# PART 2
solution_2 = 0
pos = 50
for move in input:
    direction = move[0]
    distance = int(move[1:])
    if direction == "L":
        for i in range(distance):
            pos -= 1
            if pos%100 == 0:
                solution_2 += 1
    else:
        for i in range(distance):
            pos += 1
            if pos%100 == 0:
                solution_2 += 1
    pos = pos%100

### SOLUTION 2
print("Part Two : " + str(solution_2))

submit(solution_2, part="b", day=1, year=2025)
