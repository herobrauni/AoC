# Advent of code Year 2015 Day 11 solution
# Author = brauni
# Date = 2023-11-17
"https://adventofcode.com/2015/day/11"

import re
from collections import Counter
import copy
import os
import math

solution_1, solution_2 = 0, 0

# with open(os.getcwd() + "/2015/11/example.txt", 'r') as f:
with open(os.getcwd() + "/AoC_private/2015/11/input.txt", "r") as f:
    input = f.read()
    # input = input.split("\n")
    # input = []
    # for line in f.readlines():
    # input.append(int(line))
    # input = [int(line) for line in f.readlines()]
    # input = [line for line in f.readlines()]

# PART 0


print(input)


# PART 1
def increment(pw):
    z = [ord(x) for x in pw]
    # print(z)
    # z = z.reverse()
    for i in range(len(pw) - 1, 0, -1):
        z[i] += 1
        if z[i] > 122:
            z[i] = 97
            continue
        break
    # z = z.reverse()
    return "".join([chr(x) for x in z])


def isvalid(pw):
    if re.search(r"i|o|l", pw):
        return False
    elif not len(re.findall(r"(\w)\1+", pw)) >= 2:
        return False
    z = [ord(x) for x in pw]
    for i in range(len(pw) - 3):
        if z[i] + 1 == z[i + 1] and z[i + 1] + 1 == z[i + 2]:
            return True
    return False


pw = input
while True:
    pw = increment(pw)
    if isvalid(pw):
        solution_1 = pw
        break

# PART 2
pw = solution_1
while True:
    pw = increment(pw)
    if isvalid(pw):
        solution_2 = pw
        break

# SOLUTIONS

print("Part One : " + str(solution_1) + "\nPart Two : " + str(solution_2))
