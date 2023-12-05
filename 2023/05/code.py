# Advent of code Year 2023 Day 5 solution
# Author = brauni
# Date = 2023-12-05
"https://adventofcode.com/2023/day/5"

import re
from collections import Counter
import copy
import os
import math
import numpy as np

solution_1, solution_2 = 0, 0

# with open(os.getcwd() + "/2023/05/example.txt", "r") as f:
with open(os.getcwd() + "/2023/05/input.txt", "r") as f:
    input = f.read()
    input = input.split("\n\n")
    # input = []
    # for line in f.readlines():
    # input.append(int(line))
    # input = [int(line) for line in f.readlines()]
# input = [line for line in f.readlines()]

# PART 0


print(input)


# PART 1
seeds = [int(x) for x in re.findall("\d+", input[0])]
# destination source range
#   50          98      2
#   52          50      48
tmp = input[1].split("\n")[1:]
maps = {
    key: {}
    for key in [
        "seed_to_soil",
        "soil_to_fertilizer",
        "fertilizer_to_water",
        "water_to_light",
        "light_to_temperature",
        "temperature_to_humidity",
        "humidity_to_location",
    ]
}

for c, z in enumerate(maps):
    tmp = input[c + 1].split("\n")[1:]
    for x in tmp:
        dest, source, ran = [int(y) for y in x.split()]
        maps[z][range(source, source + ran)] = range(dest, dest + ran)

locations = []
for seed in seeds:
    seed_og = seed
    for y in maps:
        for s in maps[y]:
            if seed in s:
                seed = seed - s[0] + maps[y][s][0]
                break
        # print(y, seed_og, seed)
    # print(seed_og, seed)
    locations.append(seed)

locations.sort()
solution_1 = locations[0]


# PART 2
test = []
seed_ranges = [
    range(seeds[x], seeds[x] + seeds[x + 1]) for x in range(0, len(seeds), 2)
]
# for s in maps["humidity_to_location"]:
#     for i in maps["humidity_to_location"][s]:
#         test.append(i)

p2_map = dict(reversed(maps.items()))
for x in p2_map:
    p2_map[x] = {v: k for k, v in p2_map[x].items()}

for seed in range(11627841,237692106):
    seed_og = seed

    for y in p2_map:
        for s in p2_map[y]:
            if seed in s:
                seed = seed - s[0] + p2_map[y][s][0]
                break
        # print(y, seed_og, seed)
    # print(seed_og, seed)
    if [True for x in seed_ranges if seed in x]:
        solution_2 = seed_og
        break
    if seed_og%100000 ==0:
        print(seed_og)

# locations.sort()
# solution_2 = locations[0]


# SOLUTIONS

print("Part One : " + str(solution_1) + "\nPart Two : " + str(solution_2))
