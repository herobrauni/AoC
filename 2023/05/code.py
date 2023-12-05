# Advent of code Year 2023 Day 5 solution
# Author = brauni
# Date = 2023-12-05
"https://adventofcode.com/2023/day/5"

import re
from collections import Counter
import copy
import os
import math


solution_1, solution_2 = 99999999999999999, 0

# with open(os.getcwd() + "/2023/05/example.txt", "r") as f:
with open(os.getcwd() + "/AoC_private/2023/05/input.txt", "r") as f:
    input = f.read()
    input = input.split("\n\n")


# PART 0

# print(input)


# PART 1
seeds = [int(x) for x in re.findall(r"\d+", input[0])]
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

for seed in seeds:
    seed_og = seed
    for y in maps:
        for s in maps[y]:
            if seed in s:
                seed = seed - s[0] + maps[y][s][0]
                break
        # print(y, seed_og, seed)
    # print(seed_og, seed)
    solution_1 = seed if seed < solution_1 else solution_1


# PART 2
seed_ranges = [
    range(seeds[x], seeds[x] + seeds[x + 1]) for x in range(0, len(seeds), 2)
]

# reverse the maps (so location first)
p2_map = dict(reversed(maps.items()))
# switch keys and values (because we reversed the maps)
for x in p2_map:
    p2_map[x] = {v: k for k, v in p2_map[x].items()}

location = 0
found_seed = False
while True:
    seed = location
    for y in p2_map:
        for s in p2_map[y]:
            if seed in s:
                seed = seed - s[0] + p2_map[y][s][0]
                break
    # Count backwards if we found any location that relates to a seed
    if any(seed in x for x in seed_ranges):
        location -= 1
        found_seed = True
    # Count forward and overshoot the seed until we found one that exists
    elif not found_seed:
        location += 10000
    else:
        break

solution_2 = location + 1
# SOLUTIONS

print("Part One : " + str(solution_1) + "\nPart Two : " + str(solution_2))
