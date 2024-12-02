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

# with open(os.getcwd() + "\\2021\\16\\example.txt", 'r') as f:
with open(os.getcwd() + "\\2021\\16\\input.txt", "r") as f:
    # input = f.read()
    # input = input.split("\n")
    # input = []
    # for line in f.readlines():
    # input.append(int(line))
    # input = []
    input = [bin(int("1" + line, 16))[3:] for line in f.readlines()]
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
# Type 0 = sum // done
# Type 1 = multiply
# Type 2 = Min
# Type 3 = Max
# Type 4 = literal value
# Type 5 = greater than -> 1 if sub 0 > sub 1
# Type 6 = less than -> 1 if sub 0 < sub 1
# Type 7 = equal to -> 1 if sub 0 == sub 1


def decode_package(package, pos):
    version = int("".join(package[pos : pos + 3]), 2)
    pos += 3
    type_id = int("".join(package[pos : pos + 3]), 2)
    pos += 3
    if type_id == 0:
        return type0(package, pos)
    if type_id == 1:
        return type1(package, pos)
    if type_id == 2:
        return type2(package, pos)
    if type_id == 3:
        return type3(package, pos)
    if type_id == 5:
        return type5(package, pos)
    if type_id == 6:
        return type6(package, pos)
    if type_id == 7:
        return type7(package, pos)
    elif type_id == 4:
        sub_packs = []
        while package[pos] != "0":
            sub_packs += package[pos + 1 : pos + 5]
            pos += 5
        sub_packs += package[pos + 1 : pos + 5]
        pos += 5
        value = int("".join(sub_packs), 2)
        return pos, value


def type0(package, pos):
    length_type_id = package[pos]
    pos += 1
    value = 0
    if length_type_id == "0":  # conatains length amount of bytes for subpackages
        length = int("".join(package[pos : pos + 15]), 2)
        pos += 15
        target_pos = pos + length
        while pos < target_pos:
            t1, t2 = decode_package(package, pos)
            pos = t1
            value += t2
    elif length_type_id == "1":  # contains length amount of subpackages
        length = int("".join(package[pos : pos + 11]), 2)
        pos += 11
        while length > 0:
            t1, t2 = decode_package(package, pos)
            pos = t1
            length -= 1
            value += t2
    return pos, value


def type1(package, pos):
    length_type_id = package[pos]
    pos += 1
    value = 1
    if length_type_id == "0":  # conatains length amount of bytes for subpackages
        length = int("".join(package[pos : pos + 15]), 2)
        pos += 15
        target_pos = pos + length
        while pos < target_pos:
            t1, t2 = decode_package(package, pos)
            pos = t1
            value = value * t2
    elif length_type_id == "1":  # contains length amount of subpackages
        length = int("".join(package[pos : pos + 11]), 2)
        pos += 11
        while length > 0:
            t1, t2 = decode_package(package, pos)
            pos = t1
            length -= 1
            value = value * t2
    return pos, value


def type2(package, pos):
    length_type_id = package[pos]
    pos += 1
    value = 99999999999999
    if length_type_id == "0":  # conatains length amount of bytes for subpackages
        length = int("".join(package[pos : pos + 15]), 2)
        pos += 15
        target_pos = pos + length
        while pos < target_pos:
            t1, t2 = decode_package(package, pos)
            pos = t1
            value = min(value, t2)
    elif length_type_id == "1":  # contains length amount of subpackages
        length = int("".join(package[pos : pos + 11]), 2)
        pos += 11
        while length > 0:
            t1, t2 = decode_package(package, pos)
            pos = t1
            length -= 1
            value = min(value, t2)
    return pos, value


def type3(package, pos):
    length_type_id = package[pos]
    pos += 1
    value = -99999999999999
    if length_type_id == "0":  # conatains length amount of bytes for subpackages
        length = int("".join(package[pos : pos + 15]), 2)
        pos += 15
        target_pos = pos + length
        while pos < target_pos:
            t1, t2 = decode_package(package, pos)
            pos = t1
            value = max(value, t2)
    elif length_type_id == "1":  # contains length amount of subpackages
        length = int("".join(package[pos : pos + 11]), 2)
        pos += 11
        while length > 0:
            t1, t2 = decode_package(package, pos)
            pos = t1
            length -= 1
            value = max(value, t2)
    return pos, value


def type5(package, pos):
    length_type_id = package[pos]
    pos += 1
    temp = []
    if length_type_id == "0":  # conatains length amount of bytes for subpackages
        length = int("".join(package[pos : pos + 15]), 2)
        pos += 15
        target_pos = pos + length
        while pos < target_pos:
            t1, t2 = decode_package(package, pos)
            pos = t1
            temp.append(t2)
    elif length_type_id == "1":  # contains length amount of subpackages
        length = int("".join(package[pos : pos + 11]), 2)
        pos += 11
        while length > 0:
            t1, t2 = decode_package(package, pos)
            pos = t1
            length -= 1
            temp.append(t2)
    value = 1 if temp[0] > temp[1] else 0
    return pos, value


def type6(package, pos):
    length_type_id = package[pos]
    pos += 1
    temp = []
    if length_type_id == "0":  # conatains length amount of bytes for subpackages
        length = int("".join(package[pos : pos + 15]), 2)
        pos += 15
        target_pos = pos + length
        while pos < target_pos:
            t1, t2 = decode_package(package, pos)
            pos = t1
            temp.append(t2)
    elif length_type_id == "1":  # contains length amount of subpackages
        length = int("".join(package[pos : pos + 11]), 2)
        pos += 11
        while length > 0:
            t1, t2 = decode_package(package, pos)
            pos = t1
            length -= 1
            temp.append(t2)
    value = 1 if temp[0] < temp[1] else 0
    return pos, value


def type7(package, pos):
    length_type_id = package[pos]
    pos += 1
    temp = []
    if length_type_id == "0":  # conatains length amount of bytes for subpackages
        length = int("".join(package[pos : pos + 15]), 2)
        pos += 15
        target_pos = pos + length
        while pos < target_pos:
            t1, t2 = decode_package(package, pos)
            pos = t1
            temp.append(t2)
    elif length_type_id == "1":  # contains length amount of subpackages
        length = int("".join(package[pos : pos + 11]), 2)
        pos += 11
        while length > 0:
            t1, t2 = decode_package(package, pos)
            pos = t1
            length -= 1
            temp.append(t2)
    value = 1 if temp[0] == temp[1] else 0
    return pos, value


decode_package(inp, 0)


# assert d[3] == '000000000011011'

# PART 2
# SOLUTIONS
# print("Part One : " + str(solution_1) + "\nPart Two : " + str(solution_2))
