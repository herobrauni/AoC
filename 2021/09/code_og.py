# Advent of code Year 2021 Day 9 solution
# Author = brauni
# Date = 2021-12-09
"https://adventofcode.com/2021/day/9"

import re
from collections import Counter
import copy
import os

solution_1, solution_2 = 0, 0

# with open(os.getcwd() + "\\2021\\09\\example.txt", 'r') as f:
with open(os.getcwd() + "\\2021\\09\\input.txt", "r") as f:
    input = f.read()
    input = input.split("\n")
    # input = []
    # for line in f.readlines():
    # input.append(int(line))
    # input = [int(line) for line in f.readlines()]
    # input = [line for line in f.readlines()]

# PART 0
inp = []
for line in input:
    inp.append(list(map(int, str(line))))

"""
print(input)
"""
# if inp[i][j] < inp[i-1][j] and inp[i][j] < inp[i][j-1] and inp[i][j] < inp[i+1][j] and inp[i][j] < inp[i][j+1]:
# PART 1
lowpoints = []
lowpoint_coordinates = []
for i in range(len(inp)):
    if i == 0:
        for j in range(len(inp[i])):
            if j == 0:
                if inp[i][j] < inp[i + 1][j] and inp[i][j] < inp[i][j + 1]:
                    lowpoints.append(inp[i][j])
                    lowpoint_coordinates.append([i, j])
            elif j == len(inp[i]) - 1:
                if inp[i][j] < inp[i + 1][j] and inp[i][j] < inp[i][j - 1]:
                    lowpoints.append(inp[i][j])
                    lowpoint_coordinates.append([i, j])
            else:
                if (
                    inp[i][j] < inp[i + 1][j]
                    and inp[i][j] < inp[i][j - 1]
                    and inp[i][j] < inp[i][j + 1]
                ):
                    lowpoints.append(inp[i][j])
                    lowpoint_coordinates.append([i, j])
    elif i == len(inp) - 1:
        for j in range(len(inp[i])):
            if j == 0:
                if inp[i][j] < inp[i - 1][j] and inp[i][j] < inp[i][j + 1]:
                    lowpoints.append(inp[i][j])
                    lowpoint_coordinates.append([i, j])
            elif j == len(inp[i]) - 1:
                if inp[i][j] < inp[i - 1][j] and inp[i][j] < inp[i][j - 1]:
                    lowpoints.append(inp[i][j])
                    lowpoint_coordinates.append([i, j])
            else:
                if (
                    inp[i][j] < inp[i - 1][j]
                    and inp[i][j] < inp[i][j - 1]
                    and inp[i][j] < inp[i][j + 1]
                ):
                    lowpoints.append(inp[i][j])
                    lowpoint_coordinates.append([i, j])
    else:
        for j in range(len(inp[i])):
            if j == 0:
                if (
                    inp[i][j] < inp[i - 1][j]
                    and inp[i][j] < inp[i][j + 1]
                    and inp[i][j] < inp[i + 1][j]
                ):
                    lowpoints.append(inp[i][j])
                    lowpoint_coordinates.append([i, j])
            elif j == len(inp[i]) - 1:
                if (
                    inp[i][j] < inp[i - 1][j]
                    and inp[i][j] < inp[i][j - 1]
                    and inp[i][j] < inp[i + 1][j]
                ):
                    lowpoints.append(inp[i][j])
                    lowpoint_coordinates.append([i, j])
            else:
                if (
                    inp[i][j] < inp[i - 1][j]
                    and inp[i][j] < inp[i][j - 1]
                    and inp[i][j] < inp[i][j + 1]
                    and inp[i][j] < inp[i + 1][j]
                ):
                    lowpoints.append(inp[i][j])
                    lowpoint_coordinates.append([i, j])


for x in lowpoints:
    solution_1 += x + 1
# PART 2
test = copy.deepcopy(inp)
for line in test:
    line.insert(0, 9)
    line.append(9)
border = [9] * len(test[0])
test.insert(0, border)
test.append(border)

for line in test:
    print(line)


def check_neighbours(inp, i, j):
    if inp[i][j] == 9:
        return 0
    else:
        inp[i][j] = 9
    return (
        1
        + check_neighbours(inp, i - 1, j)
        + check_neighbours(inp, i + 1, j)
        + check_neighbours(inp, i, j - 1)
        + check_neighbours(inp, i, j + 1)
    )


clusters = []
for coord in lowpoint_coordinates:
    clusters.append(check_neighbours(test, coord[0] + 1, coord[1] + 1))

clusters.sort(reverse=True)

solution_2 = clusters[0] * clusters[1] * clusters[2]

# SOLUTIONS
print("Part One : " + str(solution_1) + "\nPart Two : " + str(solution_2))
