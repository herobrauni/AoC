# Advent of Code Year 2024 Day 3 solution
# Author = brauni
# Date = 2024-12-03

import re
import os
from aocd import submit
from aocd.models import Puzzle
puzzle = Puzzle(year=2024, day=3)


# with open(os.getcwd() + "/2024/03/example.txt", 'r') as f:
with open(os.getcwd() + "/AoC_private/2024/03/input.txt", 'r') as f:
    input = f.read()
    # input = input.split("\n")
    # input = []
    # for line in f.readlines():
    # input.append(int(line))
    # input = [int(line) for line in f.readlines()]
    # input = [line for line in f.readlines()]

print(input)

# PART 1
solution_1 = 0
matches = re.findall(r'mul\(\d+,\d+\)', input)
for line in matches:
    line = line.replace('mul(', '').replace(')', '')
    x, y = line.split(",")
    solution_1 += int(x) * int(y)

# PART 2
solution_2 = 0
dont = re.finditer(r'don\'t\(\)', input)
do = re.finditer(r'do\(\)', input)
mul = re.finditer(r'mul\(\d+,\d+\)', input)

donts = []
for dn in dont:
    donts.append(dn.end())
dos = []
for d in do:
    dos.append(d.end())

for m in mul:
    i = m.start()
    print(i, m.group())
    while True and i > 0:
        if i in donts:
            break
        elif i in dos or i == 1:
            line = m.group().replace('mul(', '').replace(')', '')
            x, y = line.split(",")
            solution_2 += int(x) * int(y)
            break
        i -= 1

# SOLUTIONS

print("Part One : " + str(solution_1))

submit(solution_1, part="a", day=3, year=2024)


print("Part Two : " + str(solution_2))

submit(solution_2, part="b", day=3, year=2024)
