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
with open(os.getcwd() + "/AoC_private/2021/21/input.txt", "r") as f:
    input = f.read()
    input = input.split("\n")

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

perms_3 = list(itertools.product(dirac_dice, repeat=3))
sum_perms = [sum(x) for x in perms_3]
perms_counter = Counter(sum_perms)
keys = perms_counter.keys()
# sum([perms_counter[x] for x in perms_counter if x > 7])


def roll_1(player1, player2, score1, score2, perm, turn):
    global winner
    global resets
    # print(player1, player2, score1, score2, perm, turn)
    resets += 1
    # print(turn)
    if turn == 0:
        player1 = walk(player1, perm)
        score1 += player1
        if score1 >= 21:
            return 1
    elif turn == 1:
        player2 = walk(player2, perm)
        score2 += player2
        if score2 >= 21:
            return 0
    return sum(
        [
            roll_1(player1, player2, score1, score2, x, (turn + 1) % 2)
            * perms_counter[x]
            for x in keys
        ]
    )


def roll_2(player1, player2, score1, score2, perm, turn):
    global winner
    global resets
    # print(player1, player2, score1, score2, perm, turn)
    resets += 1
    # print(turn)
    if turn == 0:
        player1 = walk(player1, perm)
        score1 += player1
        if score1 >= 21:
            return 0
    elif turn == 1:
        player2 = walk(player2, perm)
        score2 += player2
        if score2 >= 21:
            return 1
    return sum(
        [
            roll_2(player1, player2, score1, score2, x, (turn + 1) % 2)
            * perms_counter[x]
            for x in keys
        ]
    )


def walk(position, value):
    position += value
    while position > 10:
        position -= 10
    return position


# sum([1999636718756, 555669346828, 108910351592, 11451682847,
#     58308639397748, 23142061611472, 20677802906690])

winner = [0, 0]
winner[0] = sum(
    [roll_1(player1, player2, score1, score2, x, 0) * perms_counter[x] for x in keys]
)
winner[1] = sum(
    [roll_2(player1, player2, score1, score2, x, 0) * perms_counter[x] for x in keys]
)
solution_2 = max(winner[0], winner[1])


# print(winner)
# print(resets)
# PART 2

# SOLUTIONS

print("Part One : " + str(solution_1) + "\nPart Two : " + str(solution_2))
