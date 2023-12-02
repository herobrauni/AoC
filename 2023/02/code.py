# Advent of code Year 2023 Day 2 solution
# Author = brauni
# Date = 2023-12-02
"https://adventofcode.com/2023/day/2"

import re
from collections import Counter
import copy
import os
import math
import numpy as np

solution_1, solution_2 = 0, 0

# with open(os.getcwd() + "/2023/02/example.txt", "r") as f:
with open(os.getcwd() + "/2023/02/input.txt", "r") as f:
    input = f.read()
    input = input.split("\n")
    # input = []
    # for line in f.readlines():
    # input.append(int(line))
    # input = [int(line) for line in f.readlines()]
    # input = [line for line in f.readlines()]

# PART 0


print(input)


# PART 1
# 12 red cubes, 13 green cubes, and 14 blue cubes
rules = {"red": 12, "green": 13, "blue": 14}
for x in input:
    n = int(x.split()[1].replace(":", ""))
    games = x.split(":")[1].split(";")
    possible = True
    for game in games:
        y = game.split(",")
        for z in y:
            z = z.strip()
            t = z.split(" ")
            if int(t[0]) > rules[t[1]]:
                possible = False
    if possible:
        solution_1 += n

    # print(games)

# PART 2
for x in input:
    n = int(x.split()[1].replace(":", ""))
    games = x.split(":")[1].split(";")
    bla = {"red": 0, "green": 0, "blue": 0}
    for game in games:
        y = game.split(",")
        for z in y:
            z = z.strip()
            t = z.split(" ")
            if int(t[0]) > bla[t[1]]:
                bla[t[1]] = int(t[0])
    solution_2 += bla["blue"] * bla["green"] * bla["red"]

# SOLUTIONS

print("Part One : " + str(solution_1) + "\nPart Two : " + str(solution_2))
