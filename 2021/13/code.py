# Advent of code Year 2021 Day 13 solution
# Author = brauni
# Date = 2021-12-13
"https://adventofcode.com/2021/day/13"

import re
from collections import Counter
import copy
import os
import math

solution_1, solution_2 = 0, 0

# with open(os.getcwd() + "\\2021\\13\\example.txt", 'r') as f:
with open(os.getcwd() + "\\2021\\13\\input.txt", 'r') as f:
    input = f.read()
    input = input.split("\n\n")

# PART 0
# Split input into the starting Marks and the folds
numbers = input[0]
folds = input[1].split("\n")
folds = [line.split(" along ")[1] for line in folds]

# Create list with pairs of coordinates for the marks
numbers = numbers.replace("\n", ",")
numbers = numbers.split(",")
numbers2 = []
for i in numbers:
    numbers2.append(int(i))
numbers = []
for i in range(0, len(numbers2), 2):
    numbers.append(numbers2[i:i+2])

# Create the empty sheet
sheet = [" "] * (max([x[1] for x in numbers])+1)
max_y = max([x[0] for x in numbers])
for i in range(len(sheet)):
    sheet[i] = [" "] * (max_y+1)

# PART 1
# Mark the Inputs on the sheet
for i in numbers:
    sheet[i[1]][i[0]] = "#"


# Fold the sheet along the x-axis
def fold_y(sheet, y):
    for i in range(len(sheet)):
        for j in range(len(sheet[y])):
            if i < y and sheet[abs(y - i)+y][j] == "#":
                sheet[i][j] = sheet[abs(y - i)+y][j]
    return sheet[:y]


# fold the sheet along the y-axis
def fold_x(sheet, x):
    for i in range(len(sheet)):
        for j in range(len(sheet[i])):
            if j < x and sheet[i][abs(x - j)+x] == "#":
                sheet[i][j] = sheet[i][abs(x - j)+x]
    return [i[:x] for i in sheet]


# do the first fold
for line in folds[:1]:
    line = line.split("=")
    if line[0] == "y":
        sheet = fold_y(sheet, int(line[1]))
    if line[0] == "x":
        sheet = fold_x(sheet, int(line[1]))


# Count the remaining marks
for line in sheet:
    for i in line:
        if i == "#":
            solution_1 += 1


# PART 2
# Do the rest of the folds
for line in folds[1:]:
    line = line.split("=")
    if line[0] == "y":
        sheet = fold_y(sheet, int(line[1]))
    if line[0] == "x":
        sheet = fold_x(sheet, int(line[1]))


# SOLUTIONS
print("Part One : " + str(solution_1) + "\nPart Two : ")
for line in sheet:
    print("".join(line))
