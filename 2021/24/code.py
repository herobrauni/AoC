# Advent of code Year 2021 Day 24 solution
# Author = brauni
# Date = 2021-12-24
"https://adventofcode.com/2021/day/24"

import re
from collections import Counter
import copy
import os
import math

solution_1, solution_2 = 0, 0

# with open(os.getcwd() + "/2021/24/example.txt", 'r') as f:
with open(os.getcwd() + "/2021/24/input.txt", 'r') as f:
    # input = f.read()
    # input = input.split("\n")
    # input = []
    # for line in f.readlines():
    # input.append(int(line))
    # input = [int(line) for line in f.readlines()]
    input = [line.strip() for line in f.readlines()]

# PART 0
input_formated = []
for line in input:
    line = line.split(" ")
    line = [str(x) for x in line]
    input_formated.append(line)

"""
print(input)
"""

# PART 1
number = 100000000000000
number = 99999965412437 + 1
while number > 0:
    helper = {"w": 0, "x": 0, "y": 0, "z": 0}
    i = 0
    number -= 1
    if "0" in str(number):
        continue
    # print(number)
    for line in input_formated:
        if line[0] == "inp":
            helper[line[1]] = int(str(number)[i])
            i += 1
        elif line[0] == "add":
            if line[2][-1].isdigit():
                helper[line[1]] = helper[line[1]] + int(line[2])
            else:
                helper[line[1]] = helper[line[1]] + helper[line[2]]
        elif line[0] == "mul":
            if line[2][-1].isdigit():
                helper[line[1]] = helper[line[1]] * int(line[2])
            else:
                helper[line[1]] = helper[line[1]] * helper[line[2]]
        elif line[0] == "div":
            if line[2][-1].isdigit():
                # helper[line[1]] = math.floor(helper[line[1]] / int(line[2]))
                helper[line[1]] = helper[line[1]] // int(line[2])
            else:
                # helper[line[1]] = math.floor(helper[line[1]] / helper[line[2]])
                helper[line[1]] = helper[line[1]] // helper[line[2]]
        elif line[0] == "mod":
            if line[2][-1].isdigit():
                helper[line[1]] = helper[line[1]] % int(line[2])
            else:
                helper[line[1]] = helper[line[1]] % helper[line[2]]
        elif line[0] == "eql":
            if line[2][-1].isdigit():
                if helper[line[1]] == int(line[2]):
                    helper[line[1]] = 1
                else:
                    helper[line[1]] = 0
            else:
                if helper[line[1]] == helper[line[2]]:
                    helper[line[1]] = 1
                else:
                    helper[line[1]] = 0
    if helper["z"] == 0:
        solution_1 = number
        break
# print(helper)

# PART 2
# SOLUTIONS

print("Part One : " + str(solution_1) + "\nPart Two : " + str(solution_2))
