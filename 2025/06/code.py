# Advent of Code Year 2025 Day 6 solution
# Author = brauni
# Date = 2025-12-06

import re
import os
import math
from aocd import submit
from aocd.models import Puzzle
puzzle = Puzzle(year=2025, day=6)


# with open(os.getcwd() + "/2025/06/example.txt", 'r') as f:
with open(os.getcwd() + "/AoC_private/2025/06/input.txt", 'r') as f:
    input = f.read()
    input = input.split("\n")
    # input = []
    # for line in f.readlines():
    # input.append(int(line))
    # input = [int(line) for line in f.readlines()]
    # input = [line for line in f.readlines()]

print(input)


# PART 1
solution_1 = 0

input1 = [re.findall(r"\d+|\*|\+",x) for x in input]
for i in range(len(input1[0])):
    if input1[-1][i] == "+":
        solution_1 += sum([int(x[i]) for x in input1[:-1]])
    elif input1[-1][i] == "*":
        solution_1 += math.prod([int(x[i]) for x in input1[:-1]])



### SOLUTION 1
print("Part One : " + str(solution_1))

submit(solution_1, part="a", day=6, year=2025)



# PART 2
solution_2 = 0

operation = "+"
tmptmp = []
for i in range(len(input[0])):
    spacer = 0
    tmp = ""
    for j in range(len(input)):
        if input[j][i] in ["+","*"]:
            operation = input[j][i]
        elif input[j][i] == " ":
            spacer += 1
        else:
            tmp = tmp + input[j][i]
    tmptmp.append(tmp)
    if spacer == len(input) or i == len(input[0])-1:
        spacer = 0
        if operation == "+":
            solution_2 += sum([int(x) for x in tmptmp if x != ''])
            tmptmp = []
        elif operation == "*":
            solution_2 += math.prod([int(x) for x in tmptmp if x != ''])
            tmptmp = []    

    
### SOLUTION 2
print("Part Two : " + str(solution_2))

submit(solution_2, part="b", day=6, year=2025)
