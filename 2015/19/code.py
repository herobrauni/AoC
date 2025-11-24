# Advent of Code Year 2015 Day 19 solution
# Author = brauni
# Date = 2015-12-19

import re
import os
from aocd import submit
from aocd.models import Puzzle
puzzle = Puzzle(year=2015, day=19)


# with open(os.getcwd() + "/2015/19/example.txt", 'r') as f:
with open(os.getcwd() + "/AoC_private/2015/19/input.txt", 'r') as f:
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



### SOLUTION 1
print("Part One : " + str(solution_1))

submit(solution_1, part="a", day=19, year=2015)



# PART 2
solution_2 = 0



### SOLUTION 2
print("Part Two : " + str(solution_2))

submit(solution_2, part="b", day=19, year=2015)
