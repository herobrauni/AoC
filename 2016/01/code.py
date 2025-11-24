# Advent of Code Year 2016 Day 1 solution
# Author = brauni
# Date = 2016-12-01

import re
import os
from aocd import submit
from aocd.models import Puzzle
puzzle = Puzzle(year=2016, day=1)


# with open(os.getcwd() + "/2016/01/example.txt", 'r') as f:
with open(os.getcwd() + "/AoC_private/2016/01/input.txt", 'r') as f:
    input = f.read()
    input = input.split(", ")
    # input = []
    # for line in f.readlines():
    # input.append(int(line))
    # input = [int(line) for line in f.readlines()]
    # input = [line for line in f.readlines()]

print(input)

# PART 1
solution_1 = 0
directions = ["N", "E", "S", "W"]
dir_lengths = {direction: 0 for direction in directions}

cur_dir = directions[0]  # Start facing North
for d in input:
    d0 = d[0]
    d1 = int(d[1:])
    if d0 == "R":
        cur_dir = directions[(directions.index(cur_dir) + 1) % 4]
    elif d0 == "L":
        cur_dir = directions[(directions.index(cur_dir) - 1) % 4]
    dir_lengths[cur_dir] += d1

solution_1 = abs(dir_lengths["N"] - dir_lengths["S"]) + abs(dir_lengths["E"] - dir_lengths["W"])

### SOLUTION 1
print("Part One : " + str(solution_1))

submit(solution_1, part="a", day=1, year=2016)



# PART 2
solution_2 = 0



### SOLUTION 2
print("Part Two : " + str(solution_2))

# submit(solution_2, part="b", day=1, year=2016)
