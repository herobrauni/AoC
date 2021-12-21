# Advent of code Year 2021 Day 21 solution
# Author = brauni
# Date = 2021-12-21
"https://adventofcode.com/2021/day/21"

import re
from collections import Counter
import copy
import os
import math
import itertools

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
dirac_dice = list(range(1, 4))
deterministic_dice = list(range(1, 101))
score1 = 0
score2 = 0
i = 0
rolls = 0

winner = [0, 0]
resets = 0


def roll(player1, player2, score1, score2, perm, turn):
    global winner
    global resets
    # print(player1, player2, score1, score2, perm, turn)
    resets += 1
    while turn > 5:
        turn -= 6
    # print(turn)
    if turn in range(3):
        player1 = walk(player1, perm)
        score1 += player1
        if score1 >= 21:
            winner[0] += 1
            return
    elif turn in range(3, 6):
        player2 = walk(player2, perm)
        score2 += player2
        if score2 >= 21:
            winner[1] += 1
            return
    [roll(player1, player2, score1, score2, x, turn+1) for x in range(1, 4)]


def walk(position, value):
    position += value
    while position > 10:
        position -= 10
    return position


# winner = [0, 0]
[roll(player1, player2, score1, score2, x, 0) for x in range(1, 4)]

print(dirac_dice)

len(list(itertools.product(dirac_dice, repeat=21)))


print(winner)
print(resets)
# PART 2

# SOLUTIONS

# print("Part One : " + str(solution_1) + "\nPart Two : " + str(solution_2))
