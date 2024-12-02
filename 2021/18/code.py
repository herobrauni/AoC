# Advent of code Year 2021 Day 18 solution
# Author = brauni
# Date = 2021-12-18
"https://adventofcode.com/2021/day/18"

import re
from collections import Counter
import copy
import os
import math
import ast
import itertools

solution_1, solution_2 = 0, 0

# with open(os.getcwd() + "\\2021\\18\\example.txt", 'r') as f:
with open(os.getcwd() + "\\2021\\18\\input.txt", "r") as f:
    input = [line.strip() for line in f.readlines()]


def explode(line):
    inp_list_with_brackets = list(line)
    for i in range(len(inp_list_with_brackets)):
        if "".join(inp_list_with_brackets[i : i + 2]).isalnum():
            inp_list_with_brackets[i] = "".join(inp_list_with_brackets[i : i + 2])
            del inp_list_with_brackets[i + 1]

    bc = 0
    blub = -1
    for i in range(len(inp_list_with_brackets)):
        if inp_list_with_brackets[i] == "[":
            bc += 1
        elif inp_list_with_brackets[i] == "]":
            bc -= 1
        if bc > 4:
            left_deepest_element = [
                int(inp_list_with_brackets[i + 1]),
                int(inp_list_with_brackets[i + 3]),
            ]
            blub = i
            break
    if blub == -1:
        return line

    for i in range(blub, 0, -1):
        if inp_list_with_brackets[i].isalnum():
            inp_list_with_brackets[i] = (
                int(inp_list_with_brackets[i]) + left_deepest_element[0]
            )
            break
    for i in range(blub + 5, len(inp_list_with_brackets)):
        if inp_list_with_brackets[i].isalnum():
            inp_list_with_brackets[i] = (
                int(inp_list_with_brackets[i]) + left_deepest_element[1]
            )
            break
    inp_list_with_brackets = (
        inp_list_with_brackets[:blub] + ["0"] + inp_list_with_brackets[blub + 5 :]
    )
    return str("".join([str(x) for x in inp_list_with_brackets]))


def split(line):
    for i in range(len(line)):
        if line[i].isalnum() and line[i + 1].isalnum():
            inp_list_with_brackets = list(line)
            del inp_list_with_brackets[i : i + 2]
            inp_list_with_brackets.insert(
                i,
                "".join(
                    [
                        "[",
                        str(math.floor(int("".join([line[i : i + 2]])) / 2)),
                        ",",
                        str(math.ceil(int("".join([line[i : i + 2]])) / 2)),
                        "]",
                    ]
                ),
            )
            return str("".join([str(x) for x in inp_list_with_brackets]))
    return line


def addition(line, to_add):
    return "[" + line + "," + str(to_add).replace(" ", "") + "]"


def magnitude(x):
    if isinstance(x, list):
        return magnitude(x[0]) * 3 + magnitude(x[1]) * 2
    else:
        return x


def reduce(line):
    test = -1
    while line != test:
        test = line
        if line != explode(line):
            line = explode(line)
        elif line != split(line):
            line = split(line)
    return line


temp = input[0]
for i in range(1, len(input)):
    temp = addition(temp, input[i])
    temp = reduce(temp)


x = ast.literal_eval(temp)
solution_1 = magnitude(x)


perms = list(itertools.permutations(range(len(input)), 2))

for x in perms:
    temp = addition(input[x[0]], input[x[1]])
    temp = reduce(temp)
    x = ast.literal_eval(temp)
    temp_sol = magnitude(x)
    if temp_sol > solution_2:
        solution_2 = temp_sol

print("Part One : " + str(solution_1) + "\nPart Two : " + str(solution_2))
