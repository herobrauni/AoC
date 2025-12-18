# Advent of Code Year 2025 Day 10 solution
# Author = brauni
# Date = 2025-12-10

import os
from itertools import chain, combinations

from aocd import submit
from aocd.models import Puzzle

puzzle = Puzzle(year=2025, day=10)


# with open(os.getcwd() + "/2025/10/example.txt", "r") as f:
with open(os.getcwd() + "/AoC_private/2025/10/input.txt", "r") as f:
    input = f.read()
    input = input.split("\n")
    # input = []
    # for line in f.readlines():
    # input.append(int(line))
    # input = [int(line) for line in f.readlines()]
    # input = [line for line in f.readlines()]


print(input)
inp = []
for line in input:
    tmp = line.split(" ")
    light = [x for x in tmp[0] if x in [".", "#"]]
    lights = int("".join(reversed(["1" if x == "#" else "0" for x in light])), 2)
    buttons = [eval(x) for x in tmp[1:-1]]
    buts = []
    for but in buttons:
        print(but)
        if isinstance(but, int):
            buts.append(2**but)
        else:
            buts.append(sum(2**val for val in but))
    # button = [2**x if isinstance(x, int) else tuple(2**val for val in x) for x in buttons]
    joltage = [int(x) for x in tmp[-1] if x not in ["{", ",", "}"]]
    inp.append([lights, buts, joltage])

# PART 1
solution_1 = 0

for line in inp:
    print(line)
    combos = list(chain.from_iterable(combinations(line[1], r) for r in range(1, len(line[1]) + 1)))
    for combo in combos:
        found = False
        a = 0
        for x in combo:
            a = a ^ x
        if a == line[0]:
            print("match", combo, len(combo))
            solution_1 += len(combo)
            found = True
            break
        if found:
            break

### SOLUTION 1
print("Part One : " + str(solution_1))

submit(solution_1, part="a", day=10, year=2025)
