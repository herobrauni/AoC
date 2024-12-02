# Advent of code Year 2021 Day 10 solution
# Author = brauni
# Date = 2021-12-10
"https://adventofcode.com/2021/day/10"

import re
from collections import Counter
import copy
import os
import math

solution_1, solution_2 = 0, 0

# with open(os.getcwd() + "\\2021\\10\\example.txt", 'r') as f:
with open(os.getcwd() + "\\2021\\10\\input.txt", "r") as f:
    input = f.read()
    input = input.split("\n")
    # input = []
    # for line in f.readlines():
    # input.append(int(line))
    # input = [int(line) for line in f.readlines()]
    # input = [line for line in f.readlines()]

# PART 0

"""
print(input)
"""

# PART 1
scores = {")": 3, "}": 1197, "]": 57, ">": 25137}
brackets = {"(": ")", "{": "}", "[": "]", "<": ">"}
synt_e = []
ignore = []
for line in input:
    # print(line)
    c = 0
    x = []
    for i in line:
        c += 1
        if re.match(r"\<|\(|\[|\{", i):
            x.append(i)
        elif re.match(r"\)|\}|\]|\>", i):
            if i == brackets[x[-1]]:
                # print("match", i, x[-1])
                temp = x.pop(len(x) - 1)
            else:
                synt_e += i
                ignore += [line]
                break
#     print(x)
# print(synt_e)
solution_1 = sum(scores[i] for i in synt_e)

for i in ignore:
    # print(i)
    input.remove(i)

# PART 2
scores = {"(": 1, "{": 3, "[": 2, "<": 4}
missing_brackets = []
for line in input:
    # print(line)
    c = 0
    x = []
    for i in line:
        c += 1
        if re.match(r"\<|\(|\[|\{", i):
            x.append(i)
        elif re.match(r"\)|\}|\]|\>", i):
            if i == brackets[x[-1]]:
                # print("match", i, x[-1])
                temp = x.pop(len(x) - 1)
            else:
                break
    x.reverse()
    missing_brackets.append(x)

s = []
for i in missing_brackets:
    score = 0
    for j in i:
        score = score * 5 + scores[j]
    s.append(score)


s.sort()
solution_2 = s[len(s) // 2]

# SOLUTIONS

print("Part One : " + str(solution_1) + "\nPart Two : " + str(solution_2))
