# Advent of code Year 2021 Day 2 solution
# Author = brauni
# Date = 2021-12-02

import re

# with open(os.getcwd() + "\\2021\\02\\example.txt", 'r') as f:
with open(os.getcwd() + "\\2021\\02\\input.txt", 'r') as f:
    input = f.read()
    input = input.split("\n")
    # input = []
    # for line in f.readlines():
    # input.append(int(line))
    # input = [int(line) for line in f.readlines()]
    #input = [line for line in f.readlines()]

"""
print(input)
"""

# PART 1
depth, horizontal = 0, 0

# loop through all lines and split them into command and value
# change depth and horizontal by the value according to the command
for line in input:
    line = line.split(" ")
    command = line[0]
    value = int(line[1])
    if command == "forward":
        horizontal += value
    elif command == "down":
        depth += value
    elif command == "up":
        depth -= value

solution_1 = (depth*horizontal)

# PART 2
depth, horizontal, aim = 0, 0, 0

# same as P1, but depth is only changed for command "forward"
# up/down are changing new variable aim
for line in input:
    line = line.split(" ")
    command = line[0]
    value = int(line[1])
    if command == "forward":
        horizontal += value
        depth = depth + (aim * value)
    elif command == "down":
        aim += value
    elif command == "up":
        aim -= value

solution_2 = (depth*horizontal)

# SOLUTIONS
print("Part One : " + str(solution_1))

print("Part Two : " + str(solution_2))
