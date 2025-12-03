# Advent of Code Year 2025 Day 2 solution
# Author = brauni
# Date = 2025-12-02

import re
import os
from aocd import submit
from aocd.models import Puzzle
puzzle = Puzzle(year=2025, day=2)

# with open(os.getcwd() + "/2025/02/example.txt", 'r') as f:
with open(os.getcwd() + "/AoC_private/2025/02/input.txt", 'r') as f:
    input = f.read()
    input = input.split(",")
    # input = []
    # for line in f.readlines():
    # input.append(int(line))
    # input = [int(line) for line in f.readlines()]
    # input = [line for line in f.readlines()]

print(input)

# PART 1
solution_1 = 0
for ranges in input:
    start, end = ranges.split("-")
    for i in range(int(start),int(end)+1):
        i = str(i)
        a,b = i[:len(i)//2], i[len(i)//2:]
        if a == b:
            solution_1 += int(i)

### SOLUTION 1
print("Part One : " + str(solution_1))

submit(solution_1, part="a", day=2, year=2025)

# PART 2
solution_2 = set()
for ranges in input:
    start, end = ranges.split("-")
    for i in range(int(start),int(end)+1):
        i = str(i)
        found_match = False
        for a in range(2,len(i)+1):
            # print(a)
            if len(i)%a != 0:
                continue
            b = len(i)//a
            tmp = list()
            for c in range(a):
                # print(i[c*b:(c+1)*b])
                tmp.append(i[c*b:(c+1)*b])
            tmp = set(tmp)
            if len(tmp) == 1:
                print(i)
                solution_2.add(int(i))
                found_match = True
                break

solution_2 = sum(solution_2)

### SOLUTION 2
print("Part Two : " + str(solution_2))

submit(solution_2, part="b", day=2, year=2025)
