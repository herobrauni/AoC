# Advent of Code Year 2024 Day 4 solution
# Author = brauni
# Date = 2024-12-04

import os
from aocd import submit
from aocd.models import Puzzle
puzzle = Puzzle(year=2024, day=4)


# with open(os.getcwd() + "/2024/04/example.txt", 'r') as f:
with open(os.getcwd() + "/AoC_private/2024/04/input.txt", 'r') as f:
    input = f.read()
    input = input.split("\n")
    # input = []
    # for line in f.readlines():
    # input.append(int(line))
    # input = [int(line) for line in f.readlines()]
    # input = [line for line in f.readlines()]

print(input)

finds = []
# PART 1
solution_1 = 0
for i in range(len(input)):
    for j in range(len(input[i])):
        if input[i][j] == ".":
            continue
        elif input[i][j] == "X":
            # check right
            if j+3 in range(len(input[i])):
                if input[i][j+1] == "M" and input[i][j+2] == "A" and input[i][j+3] == "S":
                    solution_1 += 1
                    finds.append((i, j))
            # check left
            if j-3 in range(len(input[i])):
                if input[i][j-1] == "M" and input[i][j-2] == "A" and input[i][j-3] == "S":
                    solution_1 += 1
                    finds.append((i, j))
            # down
            if i+3 in range(len(input)):
                if input[i+1][j] == "M" and input[i+2][j] == "A" and input[i+3][j] == "S":
                    solution_1 += 1
                    finds.append((i, j))
            # up
            if i-3 in range(len(input)):
                if input[i-1][j] == "M" and input[i-2][j] == "A" and input[i-3][j] == "S":
                    solution_1 += 1
                    finds.append((i, j))

            # down right
            if j+3 in range(len(input[i])) and i+3 in range(len(input)):
                if input[i+1][j+1] == "M" and input[i+2][j+2] == "A" and input[i+3][j+3] == "S":
                    solution_1 += 1
                    finds.append((i, j))
            # down left
            if j-3 in range(len(input[i])) and i+3 in range(len(input)):
                if input[i+1][j-1] == "M" and input[i+2][j-2] == "A" and input[i+3][j-3] == "S":
                    solution_1 += 1
                    finds.append((i, j))
            # up left
            if j-3 in range(len(input[i])) and i-3 in range(len(input)):
                if input[i-1][j-1] == "M" and input[i-2][j-2] == "A" and input[i-3][j-3] == "S":
                    solution_1 += 1
                    finds.append((i, j))
            # up right
            if j+3 in range(len(input[i])) and i-3 in range(len(input)):
                if input[i-1][j+1] == "M" and input[i-2][j+2] == "A" and input[i-3][j+3] == "S":
                    solution_1 += 1
                    finds.append((i, j))


# SOLUTION 1
print("Part One : " + str(solution_1))

submit(solution_1, part="a", day=4, year=2024)

# PART 2
solution_2 = 0
middles = []
for i in range(len(input)):
    for j in range(len(input[i])):
        if i + 2 in range(len(input)) and j + 2 in range(len(input[i])):
            if input[i][j] == "M" and input[i+1][j+1] == "A" and input[i+2][j+2] == "S":
                if input[i+2][j] == "M" and input[i][j+2] == "S":
                    solution_2 += 1
                elif input[i+2][j] == "S" and input[i][j+2] == "M":
                    solution_2 += 1
            if input[i][j] == "S" and input[i+1][j+1] == "A" and input[i+2][j+2] == "M":
                if input[i+2][j] == "M" and input[i][j+2] == "S":
                    solution_2 += 1
                elif input[i+2][j] == "S" and input[i][j+2] == "M":
                    solution_2 += 1

# SOLUTION 2
print("Part Two : " + str(solution_2))

submit(solution_2, part="b", day=4, year=2024)
