# Advent of code Year 2015 Day 14 solution
# Author = brauni
# Date = 2023-11-17
"https://adventofcode.com/2015/day/14"

import re
from collections import Counter
import copy
import os
import math

solution_1, solution_2 = 0, 0

# with open(os.getcwd() + "/2015/14/example.txt", "r") as f:
with open(os.getcwd() + "/2015/14/input.txt", "r") as f:
    input = f.read()
    input = input.split("\n")

# PART 0
print(input)
infos = {}
for line in input:
    nums = [int(x) for x in re.findall(r"\d+", line)]
    infos[line.split()[0]] = nums


def distance_at_t(stats, t):
    speed, race_t, rest_t = stats
    distance = (t // (race_t + rest_t)) * speed * race_t
    distance += (
        race_t * speed
        if race_t <= (t % (race_t + rest_t))
        else (t % (race_t + rest_t)) * speed
    )
    return distance


# PART 1
t = 2503
distance_per_deer = {key: 0 for key in infos.keys()}
for deer in infos:
    distance_per_deer[deer] = distance_at_t(infos[deer], t)
solution_1 = distance_per_deer[
    sorted(distance_per_deer, key=distance_per_deer.get, reverse=True)[0]
]


# PART 2
scoring = {key: 0 for key in infos.keys()}
distance_per_deer = {key: 0 for key in infos.keys()}
tt = 2503
for t in range(1, tt + 1):
    for deer in infos:
        distance_per_deer[deer] = distance_at_t(infos[deer], t)
    max_distance = distance_per_deer[
        sorted(distance_per_deer, key=distance_per_deer.get, reverse=True)[0]
    ]
    for d in distance_per_deer:
        if distance_per_deer[d] == max_distance:
            scoring[d] += 1

solution_2 = scoring[sorted(scoring, key=scoring.get, reverse=True)[0]]


# SOLUTIONS

print("Part One : " + str(solution_1) + "\nPart Two : " + str(solution_2))
