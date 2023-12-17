# Advent of code Year 2023 Day 17 solution
# Author = brauni
# Date = 2023-12-17
"https://adventofcode.com/2023/day/17"

import re
from collections import Counter
import copy
import os
import numpy as np
import heapq

solution_1, solution_2 = 0, 0

with open(os.getcwd() + "/AoC_private/2023/17/input.txt", "r") as f:
    # with open(os.getcwd() + "/2023/17/example.txt", "r") as f:
    input = f.read()
    input = input.split("\n")


# PART 0
print(input)
ic = []
for line in input:
    ic.append([int(x) for x in line])
input = np.array(ic)


def find_path(min_steps, max_steps, end=(len(input) - 1, len(input[0]) - 1)):
    todo = [(0, (0, 0), (1, 0)), (0, (0, 0), (0, 1))]  # start heap with down and right
    seen = set()  # save calculated nodes

    while todo:
        v, pos, dir = heapq.heappop(todo)  # take smallest item from the heap
        if pos == end:  # check if we arrived at the end
            return v
        if (pos, dir) in seen:  # skip over finished nodes
            continue
        seen.add((pos, dir))  # add to seen to not calculate twice

        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        for z in range(4):  # four possible directions
            if abs(dx[z]) != abs(dir[0]) and abs(dy[z]) != abs(
                dir[1]
            ):  # use just 90° Turns
                for i in range(
                    min_steps, max_steps + 1
                ):  # calculate all steps in that direction inside step limits
                    new_x = pos[0] + dx[z] * i
                    new_y = pos[1] + dy[z] * i
                    if new_x in range(len(input)) and new_y in range(
                        len(input[0])
                    ):  # check if new coordinates are inside the grid
                        vv = sum(
                            input[(pos[0] + dx[z] * j, pos[1] + dy[z] * j)]
                            for j in range(1, i + 1)
                        )  # calculate path cost
                        heapq.heappush(
                            todo,
                            (v + vv, (new_x, new_y), (dx[z], dy[z])),
                        )  # push step to heap


solution_1 = find_path(1, 3)
solution_2 = find_path(4, 10)

# SOLUTIONS

print("Part One : " + str(solution_1) + "\nPart Two : " + str(solution_2))
