# Advent of code Year 2021 Day 20 solution
# Author = brauni
# Date = 2021-12-21
"https://adventofcode.com/2021/day/20"

import re
from collections import Counter
import copy
import os
import math

solution_1, solution_2 = 0, 0

# with open(os.getcwd() + "\\2021\\20\\example.txt", 'r') as f:
with open(os.getcwd() + "\\2021\\20\\input.txt", 'r') as f:
    input = f.read()
    input = input.split("\n\n")


# PART 0
enhance = input[0]
pic = [list(x) for x in input[1].split("\n")]


def increase_canvas(pic, n):
    for _ in range(n):
        pic.insert(0, ["."] * len(pic[0]))
        pic.append(["."] * len(pic[0]))
        for i in range(len(pic)):
            pic[i].insert(0, ".")
            pic[i].append(".")
    return pic


"""
print(input)
"""

# PART 1


def get_grid_binary(pic, x, y, filler):
    up = pic[x - 1][y] if x > 0 else filler
    down = pic[x + 1][y] if x < len(pic) - 1 else filler
    left = pic[x][y - 1] if y > 0 else filler
    right = pic[x][y + 1] if y < len(pic[0]) - 1 else filler
    up_left = pic[x - 1][y - 1] if x > 0 and y > 0 else filler
    up_right = pic[x - 1][y + 1] if x > 0 and y < len(pic[0]) - 1 else filler
    down_left = pic[x + 1][y - 1] if x < len(pic) - 1 and y > 0 else filler
    down_right = pic[x + 1][y +
                            1] if x < len(pic) - 1 and y < len(pic[0]) - 1 else filler
    middle = pic[x][y]
    bin_str = up_left + up + up_right + left + \
        middle + right + down_left + down + down_right
    return int("".join(['0' if x == "." else '1' for x in bin_str]), 2)


# for i in range(2):
#     pic = increase_canvas(pic, 1)
    new_canvas = copy.deepcopy(pic)
    for j in range(len(pic)):
        for k in range(len(pic[0])):
            new_canvas[j][k] = enhance[get_grid_binary(pic, j, k, "#")]
    pic = new_canvas


for line in pic:
    print("".join(line))

# counter = 0
# for j in range(x-1, len(pic) - (x-1)):
#     for k in range(x-1, len(pic[0]) - (x-1)):
#         if pic[j][k] == "#":
#             counter += 1
# solution_1 = counter

solution_1 = Counter([item for sublist in pic for item in sublist])["#"]


# PART 2


# SOLUTIONS

print("Part One : " + str(solution_1) + "\nPart Two : " + str(solution_2))
