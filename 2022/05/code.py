# Advent of code Year 2022 Day 5 solution
# Author = brauni
# Date = 2022-12-05
"https://adventofcode.com/2022/day/5"

import re
from collections import Counter
import copy
import os
import math

solution_1, solution_2 = [], []

# with open(os.getcwd() + "/2022/05/example.txt", 'r') as f:
with open(os.getcwd() + "/AoC_private/2022/05/input.txt", "r") as f:
    input = f.read()
    input = input.split("\n\n")
    # input = []
    # for line in f.readlines():
    # input.append(int(line))
    # input = [int(line) for line in f.readlines()]
    # input = [line for line in f.readlines()]

# PART 0
stacks = input[0].split("\n")
instructions = input[1].split("\n")

# print(input, stacks, instructions)
# print([x.strip() for x in stacks[-1:]])
stacks.pop()

# # stack1, stack2, stack3, stack4, stack5, stack6, stack7, stack8, stack9 = [], [], [], [], [], [], [], [], []
test = [[], [], [], [], [], [], [], [], [], []]

for line in stacks:
    for i in range(1, len(line), 4):
        if line[i] != " ":
            print(i // 4 + 1, line[i])
            test[i // 4 + 1].append(line[i])

for line in test:
    line = line.reverse()


test
# PART 1
for line in instructions:
    line = line.split(" ")
    for i in range(0, int(line[1])):
        x = test[int(line[3])].pop()
        test[int(line[5])].append(x)

for line in test:
    if line != []:
        print(line[-1])
        solution_1.append(line[-1])
solution_1 = "".join(solution_1)

# PART 2
test = [[], [], [], [], [], [], [], [], [], []]

for line in stacks:
    for i in range(1, len(line), 4):
        if line[i] != " ":
            print(i // 4 + 1, line[i])
            test[i // 4 + 1].append(line[i])

for line in test:
    line = line.reverse()

# for i in range(0, len(test)):
#     test[i] = str("".join(test[i]))

for line in instructions:
    line = line.split(" ")
    temp = []
    for i in range(0, int(line[1])):
        test[int(line[3])] = list(test[int(line[3])])
        x = test[int(line[3])].pop()
        temp.append(x)
    temp.reverse()
    # temp = "".join(temp)
    for z in temp:
        test[int(line[5])].append(z)


for line in test:
    if line != []:
        print(line[-1])
        solution_2.append(line[-1])
solution_2 = "".join(solution_2)


# SOLUTIONS

print("Part One : " + str(solution_1) + "\nPart Two : " + str(solution_2))
