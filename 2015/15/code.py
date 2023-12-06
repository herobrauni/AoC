# Advent of code Year 2015 Day 15 solution
# Author = brauni
# Date = 2023-12-06
"https://adventofcode.com/2015/day/15"

import re
from collections import Counter
import copy
import os
import math
import itertools

solution_1, solution_2 = 0, 0

with open(os.getcwd() + "/AoC_private/2015/15/input.txt", "r") as f:
    # with open(os.getcwd() + "/2015/15/example.txt", "r") as f:
    input = f.read()
    input = input.split("\n")
    # input = []
    # for line in f.readlines():
    # input.append(int(line))
    # input = [int(line) for line in f.readlines()]
    # input = [line for line in f.readlines()]

# PART 0


print(input)
ingredients = {}
for line in input:
    ingredients[line.split(":")[0]] = [int(x) for x in re.findall(r"-?\d+", line)]

# PART 1
combinations = itertools.combinations_with_replacement(ingredients.keys(), 100)
for it in combinations:
    counts = Counter(it)
    # counts
    blub = [0, 0, 0, 0, 0]
    for x in counts:
        for n, y in enumerate(ingredients[x]):
            blub[n] += y * counts[x]
    blub = [x if x > 0 else 0 for x in blub]
    calories = blub[4]
    blub = blub[:-1]
    solution_1 = math.prod(blub) if math.prod(blub) > solution_1 else solution_1
    if calories == 500:
        # print(blub, math.prod(blub))
        solution_2 = math.prod(blub) if math.prod(blub) > solution_2 else solution_2

# [ingredients[x] * counts[x] for x in counts]
# [ingredients[x] for x in counts]


# PART 2


# SOLUTIONS

print("Part One : " + str(solution_1) + "\nPart Two : " + str(solution_2))
