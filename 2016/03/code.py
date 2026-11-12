# Advent of Code Year 2016 Day 3 solution
# Author = brauni
# Date = 2016-12-03

import re
import os
from aocd import submit
from aocd.models import Puzzle
puzzle = Puzzle(year=2016, day=3)


# with open(os.getcwd() + "/2016/03/example.txt", 'r') as f:
with open(os.getcwd() + "/AoC_private/2016/03/input.txt", 'r') as f:
    input = [list(map(int, line.split())) for line in f if line.strip()]

print(input)

# PART 1
solution_1 = 0

for inp in input:
    a, b, c = sorted(inp)
    if a + b > c:
        solution_1 += 1


### SOLUTION 1
print("Part One : " + str(solution_1))

submit(solution_1, part="a", day=3, year=2016)



# PART 2
solution_2 = 0

for col in range(3):
    column = [row[col] for row in input]
    for i in range(0, len(column), 3):
        a, b, c = sorted(column[i:i + 3])
        if a + b > c:
            solution_2 += 1



### SOLUTION 2
print("Part Two : " + str(solution_2))

submit(solution_2, part="b", day=3, year=2016)
