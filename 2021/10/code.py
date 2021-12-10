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
with open(os.getcwd() + "\\2021\\10\\input.txt", 'r') as f:
    input = f.read()
    input = input.split("\n")
# PART 0

"""
print(input)
"""

# PART 1
scores = {")": 3, "}": 1197,
          "]": 57, ">": 25137, "(": 1, "{": 3, "[": 2, "<": 4}
brackets = {"(": ")", "{": "}", "[": "]", "<": ">",
            ")": "(", "}": "{", "]": "[", ">": "<"}
synt_e = []
ignore = []
# Iterate through the input by line and by character
for line in input:
    x = []
    for i in line:
        # if the char is a opening bracket add it to the list
        if i in "<({[":
            x.append(i)
        # if the char is a closing bracket check if the last opening bracket is the same
        # if it is we remove it from the list, otherwise we found a corrupted line and add it to the solution
        # add the line to ignore to remove it from the input before p2
        elif i in ">)}]":
            if i == brackets[x[-1]]:
                temp = x.pop(len(x) - 1)
            else:
                solution_1 += scores[i]
                ignore += [line]
                break

# Remove lines already done in p1
for i in ignore:
    input.remove(i)

# PART 2
missing_brackets = []
# Iterate through the remaining input, line by line and character by character
for line in input:
    x = []
    # add opening brackets to the list
    # if a closing bracket is found, check if the last opening bracket is the same
    # if so, remove it from the list, so we end up with a list of unclosed opening brackets
    for i in line:
        if i in "<({[":
            x.append(i)
        elif i in ">)}]":
            if i == brackets[x[-1]]:
                temp = x.pop(len(x) - 1)
    # Reverse the list to have the correct order for the closing brackets
    x.reverse()
    missing_brackets.append(x)

# Calculate the score for each line
s = []
for i in missing_brackets:
    score = 0
    for j in i:
        score = score*5 + scores[j]
    s.append(score)

# Select the middle score
s.sort()
solution_2 = s[len(s)//2]

# SOLUTIONS

print("Part One : " + str(solution_1) + "\nPart Two : " + str(solution_2))
