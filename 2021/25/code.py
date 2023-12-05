# Advent of code Year 2021 Day 25 solution
# Author = brauni
# Date = 2021-12-25
"https://adventofcode.com/2021/day/25"

import re
from collections import Counter
import copy
import os
import math

solution_1, solution_2 = 0, 0

# with open(os.getcwd() + "/2021/25/example.txt", 'r') as f:
with open(os.getcwd() + "/AoC_private/2021/25/input.txt", "r") as f:
    input = f.read()
    input = input.split("\n")
    # input = []
    # for line in f.readlines():
    # input.append(int(line))
    # input = [int(line) for line in f.readlines()]
    # input = [line.strip() for line in f.readlines()]

# PART 0
input_formated = []
for line in input:
    line = [x for x in line]
    input_formated.append(line)

for line in input_formated:
    print(line)

move_arr = []
# for line in input_formated:
# move_arr.append(['.' for x in line])


def move_until_done(input_formated):
    n = 1
    moves = 0
    while n != 0:
        moves += 1
        # print(moves)
        n = 0
        move_arr = []
        for i in range(len(input_formated)):
            # EAST
            for j in range(len(input_formated[i])):
                if j < len(input_formated[i]) - 1:
                    if input_formated[i][j] == ">" and input_formated[i][j + 1] == ".":
                        move_arr.append([i, j, i, j + 1])
                elif input_formated[i][j] == ">" and input_formated[i][0] == ".":
                    move_arr.append([i, j, i, 0])
        for line in move_arr:
            n += 1
            input_formated[line[0]][line[1]] = "."
            input_formated[line[2]][line[3]] = ">"
            # DOWN
        move_arr = []
        for i in range(len(input_formated)):
            for j in range(len(input_formated[i])):
                if i < len(input_formated) - 1:
                    if input_formated[i][j] == "v" and input_formated[i + 1][j] == ".":
                        move_arr.append([i, j, i + 1, j])
                elif input_formated[i][j] == "v" and input_formated[0][j] == ".":
                    move_arr.append([i, j, 0, j])
        for line in move_arr:
            n += 1
            input_formated[line[0]][line[1]] = "."
            input_formated[line[2]][line[3]] = "v"
    global solution_1
    solution_1 = moves
    return input_formated


input_formated = move_until_done(input_formated)

for line in input_formated:
    print("".join([str(x) for x in line]))

"""
print(input)
"""

# PART 1

# PART 2

# SOLUTIONS

print("Part One : " + str(solution_1) + "\nPart Two : " + str(solution_2))
