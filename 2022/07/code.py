# Advent of code Year 2022 Day 7 solution
# Author = brauni
# Date = 2022-12-07
"https://adventofcode.com/2022/day/7"

import re
from collections import Counter
import copy
import os
import math

solution_1, solution_2 = 0, 0

# with open(os.getcwd() + "/2022/07/example.txt", 'r') as f:
with open(os.getcwd() + "/2022/07/input.txt", 'r') as f:
    input = f.read()
    input = input.split("\n")
    # input = []
    # for line in f.readlines():
    # input.append(int(line))
    # input = [int(line) for line in f.readlines()]
    # input = [line for line in f.readlines()]

# PART 0


print(input)

all = {}
current = []
i = 0

# PART 1
for i in range(0, len(input)):
    if input[i].split()[1] == "cd" and input[i].split()[2] != "..":
        # print(input[i])
        current.append(input[i].split()[2])
    if input[i].split()[1] == "cd" and input[i].split()[2] == "..":
        null = current.pop()
    if input[i].split()[1] == "ls":
        z = "-".join([str(x) for x in current])
        all[z] = []
        i += 1
        while(input[i].split()[0] != "$"):
            if input[i].split()[0].isdigit():
                all[z].append(input[i].split()[0])
            elif input[i].split()[0] == "dir":
                all[z].append(z + "-" + input[i].split()[1])
            i += 1
            if i >= len(input):
                break


def calculate(l):
    if isinstance(l[0], list):
        return sum([calculate(x) for x in l])
    elif len([x for x in l if not x.isdigit()]):
        return sum([int(x) for x in l if x.isdigit()]) + sum([calculate(all[x]) for x in l if not x.isdigit()])
    else:
        return sum([int(x) for x in l])


combined = {}

for key in all:
    # print(key)
    combined[key] = calculate(all[key])

for line in combined:
    if combined[line] <= 100000:
        solution_1 += combined[line]

# l = all["/"]
# PART 2
total = 70000000
needed = 30000000
fr = total - combined["/"]
to_free = needed - fr

free_dict = {}

for line in combined:
    if combined[line] >= to_free:
        free_dict[line] = combined[line]

list_2 = list(free_dict.values())
list_2.sort()
solution_2 = list_2[0]

# SOLUTIONS
print("Part One : " + str(solution_1) + "\nPart Two : " + str(solution_2))
