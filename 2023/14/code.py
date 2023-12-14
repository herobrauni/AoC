# Advent of code Year 2023 Day 14 solution
# Author = brauni
# Date = 2023-12-14
"https://adventofcode.com/2023/day/14"

import re
from collections import Counter
import copy
import os
import math
import numpy as np


solution_1, solution_2 = 0, 0

with open(os.getcwd() + "/AoC_private/2023/14/input.txt", "r") as f:
    # with open(os.getcwd() + "/2023/14/example.txt", "r") as f:
    input = f.read()


# PART 0
def tilt(input, direction):
    input = input.split("\n")
    ic = []
    for line in input:
        ic.append([x for x in line])
    input = ic

    move = True
    while move:
        move = False
        match direction:
            # north
            case "north":
                for n in range(len(input)):
                    for i in range(len(input[n])):
                        try:
                            if input[n + 1][i] == "O" and input[n][i] == ".":
                                input[n + 1][i] = "."
                                input[n][i] = "O"
                                move = True
                        except IndexError:
                            pass
            case "south":
                l = len(input)
                for n in range(len(input)):
                    for i in range(len(input[n])):
                        try:
                            if input[l - n - 1][i] == "O" and input[l - n][i] == ".":
                                input[l - n - 1][i] = "."
                                input[l - n][i] = "O"
                                move = True
                        except IndexError:
                            pass
            case "west":
                for n in range(len(input)):
                    for i in range(len(input[n])):
                        try:
                            if input[n][i + 1] == "O" and input[n][i] == ".":
                                input[n][i + 1] = "."
                                input[n][i] = "O"
                                move = True
                        except IndexError:
                            pass
            case "east":
                l = len(input[0])
                for n in range(len(input)):
                    for i in range(len(input[n])):
                        try:
                            if input[n][l - i - 1] == "O" and input[n][l - i] == ".":
                                input[n][l - i - 1] = "."
                                input[n][l - i] = "O"
                                move = True
                        except IndexError:
                            pass
    input = "\n".join(["".join(x) for x in input])
    # test[(og_input, direction)] = input
    return input


def score(input):
    s = 0
    input = input.split("\n")
    ic = []
    for line in input:
        ic.append([x for x in line])
    input = ic

    for n in range(len(input)):
        for x in input[n]:
            if x == "O":
                s += len(input) - n
    return s


# PART 1
solution_1 = score(tilt(input,"north"))

# PART 2
test = {}
scores = []
cycle = 0
goal = 1000000000

cycle_found = False

while cycle < goal:
    for direction in ["north", "west", "south", "east"]:
        input = tilt(input, direction)
    cycle += 1

    if not cycle_found and (cycle_found := input in test):
        cycle_l = cycle - test[input]
        cycle += cycle_l * ((goal - cycle) // cycle_l)
    else:
        test[input] = cycle

solution_2 = score(input)


# SOLUTIONS

print("Part One : " + str(solution_1) + "\nPart Two : " + str(solution_2))
