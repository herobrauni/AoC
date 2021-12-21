# Advent of code Year 2021 Day 21 solution
# Author = brauni
# Date = 2021-12-21
"https://adventofcode.com/2021/day/21"

import re
from collections import Counter
import copy
import os
import math

solution_1, solution_2 = 0, 0

# with open(os.getcwd() + "/2021/21/example.txt", 'r') as f:
with open(os.getcwd() + "/2021/21/input.txt", 'r') as f:
    input = f.read()
    input = input.split("\n")
    # input = []
    # for line in f.readlines():
    # input.append(int(line))
    # input = [int(line) for line in f.readlines()]
    # input = [line for line in f.readlines()]

# PART 0
player1 = int(input[0][-1])
player2 = int(input[1][-1])
"""
print(input)
"""

# PART 1
deterministic_dice = list(range(1, 101))
score1 = 0
score2 = 0
i = 0
rolls = 0
while score1 < 1000 and score2 < 1000:
    for x in range(3):
        player1 += deterministic_dice[i]
        i += 1
        rolls += 1
        if i == len(deterministic_dice):
            i = 0
        while player1 > 10:
            player1 -= 10
    score1 += player1
    # print(score1)
    if score1 >= 1000:
        break
    for x in range(3):
        player2 += deterministic_dice[i]
        i += 1
        rolls += 1
        if i == len(deterministic_dice):
            i = 0
        while player2 > 10:
            player2 -= 10
    score2 += player2
    # print(score2)
    if score2 >= 1000:
        break

solution_1 = min(score1, score2) * rolls

# PART 2

# SOLUTIONS

print("Part One : " + str(solution_1) + "\nPart Two : " + str(solution_2))
