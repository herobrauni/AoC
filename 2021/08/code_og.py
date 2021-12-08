# Advent of code Year 2021 Day 8 solution
# Author = brauni
# Date = 2021-12-08
"https://adventofcode.com/2021/day/8"

import re
from collections import Counter
import copy
import os

solution_1, solution_2 = 0, 0

# with open(os.getcwd() + "\\2021\\08\\example.txt", 'r') as f:
with open(os.getcwd() + "\\2021\\08\\input.txt", 'r') as f:
    input = f.read()
    input = input.split("\n")
    # input = []
    # for line in f.readlines():
    # input.append(int(line))
    # input = [int(line) for line in f.readlines()]
    # input = [line for line in f.readlines().split("|")[0]]

# PART 0
inp, out = [], []
for line in input:
    x = line.split("|")
    inp += [y.strip() for y in x[0].split()]
    out += [y.strip() for y in x[1].split()]

"""
print(input)
"""

# PART 1
count = 0
for line in out:
    if re.match(r'\b[a-g]{2,4}\b|\b[a-g]{7}\b', line):
        count += 1
solution_1 = count


# PART 2
inp, out = [], []
for line in input:
    x = line.split("|")
    inp.append([y.strip() for y in x[0].split()])
    out.append([y.strip() for y in x[1].split()])

for i in range(0, len(inp)):
    one = str([x for x in inp[i] if len(x) == 2][0])
    seven = str([x for x in inp[i] if len(x) == 3][0])
    four = str([x for x in inp[i] if len(x) == 4][0])
    eight = str([x for x in inp[i] if len(x) == 7][0])
    six_bars = [x for x in inp[i] if len(x) == 6][0:3]
    for j in six_bars:
        if len([x for x in j if x not in seven]) == 4:
            # print("six:", j)
            six = j
        elif len([x for x in j if x not in four]) == 3:
            # print('zero', j)
            zero = j
        elif len([x for x in j if x not in four]) == 2:
            # print('nine', j)
            nine = j
    five_bars = [x for x in inp[i] if len(x) == 5][0:3]
    top_right_bar = [x for x in one if x not in six][0]
    for j in five_bars:
        if len([x for x in j if x not in one]) == 3:
            three = j
        elif len([x for x in top_right_bar if x in j]) == 1:
            two = j
        else:
            five = j

    output_number = []
    for j in range(len(out[i])):
        # print(out[i][j])
        if Counter(out[i][j]) == Counter(zero):
            output_number.append(0)
        if Counter(out[i][j]) == Counter(one):
            output_number.append(1)
        if Counter(out[i][j]) == Counter(two):
            output_number.append(2)
        if Counter(out[i][j]) == Counter(three):
            output_number.append(3)
        if Counter(out[i][j]) == Counter(four):
            output_number.append(4)
        if Counter(out[i][j]) == Counter(five):
            output_number.append(5)
        if Counter(out[i][j]) == Counter(six):
            output_number.append(6)
        if Counter(out[i][j]) == Counter(seven):
            output_number.append(7)
        if Counter(out[i][j]) == Counter(eight):
            output_number.append(8)
        if Counter(out[i][j]) == Counter(nine):
            output_number.append(9)
    temp_sol = ''.join(str(x) for x in output_number)
    print(inp[i], out[i], temp_sol)
    temp_sol = int(temp_sol)
    solution_2 += temp_sol


# SOLUTIONS
print("Part One : " + str(solution_1) + "\nPart Two : " + str(solution_2))
