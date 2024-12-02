# Advent of code Year 2021 Day 6 solution
# Author = brauni
# Date = 2021-12-06
"https://adventofcode.com/2021/day/6"

import re
from collections import defaultdict, Counter
import copy
import os

solution_1, solution_2 = 0, 0

# with open(os.getcwd() + "\\2021\\06\\example.txt", 'r') as f:
with open(os.getcwd() + "\\2021\\06\\input.txt", "r") as f:
    input = f.read().strip().replace("\n", ",")

# PART 0
input = [int(x) for x in re.split(" -> |,", input)]

"""
print(input)
"""

fish_age_counter = Counter(input)


# PART 1
# get only the zero_lifetimeber of occurances of each zero_lifetimeber 0-9
fishes = [input.count(i) for i in range(9)]
for i in range(80):
    # remove count of fishes with lifetime 0 and save the ammount to zero_lifetime
    zero_lifetime = fishes.pop(0)
    # add the zero_lifetimeber of fishes with lifetime 0 to the fishes with lifetime 6 (they respawn as those)
    fishes[6] += zero_lifetime
    # add the zero_lifetimeber of fishes with lifetime 0 to the fishes as babies
    fishes.append(zero_lifetime)

solution_1 = sum(fishes)

# PART 2
fishes = [input.count(i) for i in range(9)]
for i in range(256):
    # remove count of fishes with lifetime 0 and save the ammount to zero_lifetime
    zero_lifetime = fishes.pop(0)
    # add the zero_lifetimeber of fishes with lifetime 0 to the fishes with lifetime 6 (they respawn as those)
    fishes[6] += zero_lifetime
    # add the zero_lifetimeber of fishes with lifetime 0 to the fishes as babies
    fishes.append(zero_lifetime)

solution_2 = sum(fishes)
# SOLUTIONS

print("Part One : " + str(solution_1) + "\nPart Two : " + str(solution_2))
