# Advent of code Year 2023 Day 6 solution
# Author = brauni
# Date = 2023-12-06
"https://adventofcode.com/2023/day/6"

import re
from collections import Counter
import copy
import os
import math

solution_1, solution_2 = 0, 0

with open(os.getcwd() + "/AoC_private/2023/06/input.txt", "r") as f:
    # with open(os.getcwd() + "/2023/06/example.txt", 'r') as f:
    input = f.read()
    input = input.split("\n")
    # input = []
    # for line in f.readlines():
    # input.append(int(line))
    # input = [int(line) for line in f.readlines()]
    # input = [line for line in f.readlines()]

# PART 0


print(input)
time = [int(x) for x in re.findall(r"\d+", input[0])]
record = [int(x) for x in re.findall(r"\d+", input[1])]


# PART 1
wins = []
for n, x in enumerate(time):
    win = 0
    for i in range(x):
        distance = i * (x - i)
        if distance > record[n]:
            win += 1
    print(n, win)
    wins.append(win)
solution_1 = math.prod(wins)


# PART 2
time = [int(x) for x in re.findall(r"\d+", input[0].replace(" ", ""))]
record = [int(x) for x in re.findall(r"\d+", input[1].replace(" ", ""))]

for n, x in enumerate(time):
    win = 0
    for i in range(x):
        distance = i * (x - i)
        if distance > record[n]:
            win += 1
solution_2 = win

# SOLUTIONS

print("Part One : " + str(solution_1) + "\nPart Two : " + str(solution_2))
