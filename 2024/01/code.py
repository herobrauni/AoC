# Advent of Code Year 2024 Day 1 solution
# Author = brauni
# Date = 2024-12-01

from collections import Counter
import os
from aocd import submit
from aocd.models import Puzzle
puzzle = Puzzle(year=2024, day=1)


# with open(os.getcwd() + "/2024/01/example.txt", 'r') as f:
with open(os.getcwd() + "/AoC_private/2024/01/input.txt", 'r') as f:
    input = f.read()
    input = input.split("\n")


print(input)

# PART 1
solution_1 = 0
x = [int(line.split("   ")[0]) for line in input]
y = [int(line.split("   ")[1]) for line in input]

x.sort()
y.sort()

for z in range(len(input)):
    solution_1 += abs(x[z] - y[z])

# PART 2
solution_2 = 0
bla = Counter(y)
for b in x:
    solution_2 += b * bla[b]

# SOLUTIONS

print("Part One : " + str(solution_1))

submit(solution_1, part="a", day=1, year=2024)


print("Part Two : " + str(solution_2))

submit(solution_2, part="b", day=1, year=2024)
