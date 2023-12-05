# Advent of code Year 2023 Day 4 solution
# Author = brauni
# Date = 2023-12-04
"https://adventofcode.com/2023/day/4"

import re
from collections import Counter
import copy
import os
import math
import numpy as np

solution_1, solution_2 = 0, 0

# with open(os.getcwd() + "/2023/04/example.txt", "r") as f:
with open(os.getcwd() + "/AoC_private/2023/04/input.txt", "r") as f:
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
for line in input:
    winning = re.findall("\d+", line.split(":")[1].split("|")[0])
    n = re.findall("\d+", line.split(":")[1].split("|")[1])
    winners = sum([1 for x in winning if x in n])
    solution_1 += pow(2, winners - 1) if winners > 0 else 0


# PART 2
cards = {}
for line in input:
    card = int(re.findall("\d+", line.split(":")[0])[0])
    winning = re.findall("\d+", line.split(":")[1].split("|")[0])
    n = re.findall("\d+", line.split(":")[1].split("|")[1])
    cards[card] = [1, winning, n]


for x in range(1, len(cards) + 1):
    bla = 1
    for z in cards[x][1]:
        if z in cards[x][2]:
            cards[x + bla][0] += cards[x][0]
            bla += 1

solution_2 = sum([cards[x][0] for x in cards])

# SOLUTIONS

print("Part One : " + str(solution_1) + "\nPart Two : " + str(solution_2))
