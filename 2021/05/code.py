# Advent of code Year 2021 Day 5 solution
# Author = brauni
# Date = 2021-12-05
# https://adventofcode.com/2021/day/5

import re
from collections import Counter
import copy

solution_1, solution_2 = 0, 0

# with open("C:\\Users\\brauni\\Documents\\GitHub\\AoC\\2021\\05\\example.txt", 'r') as f:
with open("C:\\Users\\brauni\\Documents\\GitHub\\AoC\\2021\\05\\input.txt", 'r') as f:
    input = f.read().strip().replace('\n', ',')

# PART 0
# Usual input processing, this time creating one big list with ALL ints, in the incoming order
input = [int(x) for x in re.split(' -> |,', input)]

# Then grouping again by pairs of 4
t1 = [input[i:i+4] for i in range(0, len(input), 4)]

# PART 1
# Creating a 2d list with size of the biggest number in the list
# +1 because 0 is included in Input
diagram = [[0]*(max(input)+1) for i in range(max(input)+1)]

# Iterate through each Pair of Coordinates
for line in t1:
    # for better readability we assign them to x1, y1, x2, y2
    x1, y1, x2, y2 = line[0], line[1], line[2], line[3]
    # We care only about Vertical and Horizontal lines
    if x1 == x2 or y1 == y2:
        # Chose smaller and bigger Number in x1,x2 for lower and upper bound
        for x in range(min(x1, x2), max(x1, x2)+1):
            # Chose smaller and bigger Number in y1,y2 for lower and upper bound
            for y in range(min(y1, y2), max(y1, y2)+1):
                # Add 1 to the diagram at the coordinates
                # y and x are swaped here to be able to print the diagram the same orientation as AoC
                diagram[y][x] += 1

# Count all Fields in the Diagram that are > 1 (crossing lines)
for line in diagram:
    for row in line:
        if row > 1:
            solution_1 += 1

# PART 2
# Creating a 2d list with size of the biggest number in the list
# +1 because 0 is included in Input
diagram = [[0]*(max(input)+1) for i in range(max(input)+1)]

# Iterate through each Pair of Coordinates
for line in t1:
    # for better readability we assign them to x1, y1, x2, y2
    x1, y1, x2, y2 = line[0], line[1], line[2], line[3]

    # Assign dx and dy depending on the direction we want to go
    # Use these later for adding to the coordinates
    dx = 1 if x1 < x2 else -1
    dy = 1 if y1 < y2 else -1

    # If line is not diagonal we assign 0 to dx for vertical and dy for horizontal
    if x1 == x2:
        dx = 0
    if y1 == y2:
        dy = 0

    # Add 1 to the diagram at the starting coordinates
    diagram[y1][x1] += 1
    # Iterate until the start and end coordinates meet/overlap/are the same
    # Add 1 to the diagram at the coordinates for each iteration
    while x1 != x2 or y1 != y2:
        x1 += dx
        y1 += dy
        diagram[y1][x1] += 1

# Count all Fields in the Diagram that are > 1 (crossing lines)
for line in diagram:
    for row in line:
        if row > 1:
            solution_2 += 1

# for line in diagram:
#     print(line)


# SOLUTIONS
print("Part One : " + str(solution_1) + "\nPart Two : " + str(solution_2))
