# Advent of code Year 2021 Day 16 solution
# Author = brauni
# Date = 2021-12-16
"https://adventofcode.com/2021/day/16"

import re
from collections import Counter
import copy
import os
import math

solution_1, solution_2 = 0, 0

with open(os.getcwd() + "\\2021\\16\\example.txt", 'r') as f:
    # with open(os.getcwd() + "\\2021\\16\\input.txt", 'r') as f:
    # input = f.read()
    # input = input.split("\n")
    # input = []
    # for line in f.readlines():
    # input.append(int(line))
    # input = []
    input = [bin(int('1'+line, 16))[3:] for line in f.readlines()]
    # input = [line for line in f.readlines()]

# PART 0
inp = []
for x in input:
    for y in x:
        inp.append(y)

"""
print(inp[2])
"""

# PART 1
# find versions
# Type = 4 -> literal value -> single binary number
# Type != 4 -> Operator


def decode_package(package, pos):
    version = "".join(package[pos:pos+3])
    pos += 3
    type_id = "".join(package[pos:pos+3])
    pos += 3
    if type_id != "100":
        length_type_id = package[pos]
        pos += 1
        if length_type_id == "0":  # conatains length amount of bytes for subpackages
            length = "".join(package[pos:pos+15])
            pos += 15
        elif length_type_id == "1":  # contains length amount of subpackages
            length = "".join(package[pos:pos+11])
            pos += 11
        return int(version, 2), int(type_id, 2), int(length_type_id, 2), length, pos
    elif type_id == "100":
        sub_packs = []
        while package[pos] != "0":
            sub_packs += package[pos+1:pos+5]
            pos += 5
        sub_packs += package[pos+1:pos+5]
        pos += 5
        value = int("".join(sub_packs), 2)
        return int(version, 2), int(type_id, 2), sub_packs, value, pos


d = decode_package(inp, 0)
print(d)
assert d[3] == '000000000011011'

# PART 2
# SOLUTIONS
# print("Part One : " + str(solution_1) + "\nPart Two : " + str(solution_2))
