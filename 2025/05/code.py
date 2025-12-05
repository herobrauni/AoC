# Advent of Code Year 2025 Day 5 solution
# Author = brauni
# Date = 2025-12-05

import re
import os
import portion as P
from aocd import submit
from aocd.models import Puzzle
puzzle = Puzzle(year=2025, day=5)


# with open(os.getcwd() + "/2025/05/example.txt", 'r') as f:
with open(os.getcwd() + "/AoC_private/2025/05/input.txt", 'r') as f:
    input = f.read()
    input = input.split("\n\n")
    # input = []
    # for line in f.readlines():
    # input.append(int(line))
    # input = [int(line) for line in f.readlines()]
    # input = [line for line in f.readlines()]

ranges = input[0].split("\n")
ingredients = input[1].split("\n")

# PART 1
solution_1 = 0

fresh = set()
for r in ranges:
    s = int(r.split("-")[0])
    e = int(r.split("-")[1])
    fresh.add(range(s,e+1))

for i in ingredients:
    for f in fresh:
        if int(i) in f:
            solution_1 += 1
            break

### SOLUTION 1
print("Part One : " + str(solution_1))

submit(solution_1, part="a", day=5, year=2025)



# PART 2
solution_2 = 0
ips = []
for r in ranges:
    s = int(r.split("-")[0])
    e = int(r.split("-")[1])
    ips.append([s,e])

pips = [P.closed(a,b) for a,b in ips]
merge = P.Interval(*pips)

solution_2 = sum([i.upper+1 - i.lower for i in merge])

### SOLUTION 2
print("Part Two : " + str(solution_2))

submit(solution_2, part="b", day=5, year=2025)
