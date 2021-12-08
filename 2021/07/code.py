# Advent of code Year 2021 Day 7 solution
# Author = brauni
# Date = 2021-12-07
"https://adventofcode.com/2021/day/7"

import re
from collections import Counter
import copy
import os

solution_1, solution_2 = 0, 0

# with open(os.getcwd() + "\\2021\\07\\example.txt", 'r') as f:
with open(os.getcwd() + "\\2021\\07\\input.txt", 'r') as f:
    input = f.read()


# PART 0
# Split on "," and cast as Int -> List with elements as Int
input = [int(line) for line in input.split(",")]

"""
print(input)
"""

# PART 1
fuel = []
# Range as Smallest and Largest Position in Startingpositions of the Crabs
for i in range(min(input), max(input)+1):
    f = 0
    # iterate over the input and add the fuel for each position
    for j in range(len(input)):
        f += (abs(input[j]-i))
    fuel.append(f)

# Select the least fuel used
solution_1 = min(fuel)


# PART 2
fuel = []
# Range as Smallest and Largest Position in Startingpositions of the Crabs
for i in range(min(input), max(input)+1):
    f = 0
    # iterate over the input and add the fuel for each position
    for j in range(len(input)):
        # 1/2 n (1 + n) <-> Gaußsche Summenformel # Thanks WolframAlpha
        f += (1/2)*(abs(input[j]-i))*(1 + abs(input[j]-i))
    fuel.append(f)

# Select the least fuel used
solution_2 = int(min(fuel))


# SOLUTIONS

print("Part One : " + str(solution_1) + "\nPart Two : " + str(solution_2))
