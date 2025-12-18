# Advent of Code Year 2025 Day 9 solution
# Author = brauni
# Date = 2025-12-09

import itertools
import os

from aocd import submit
from aocd.models import Puzzle
from shapely import Polygon

puzzle = Puzzle(year=2025, day=9)


# with open(os.getcwd() + "/2025/09/example.txt", "r") as f:
with open(os.getcwd() + "/AoC_private/2025/09/input.txt", "r") as f:
    input = f.read()
    input = [
        complex(int(line.split(",")[0]), int(line.split(",")[1]))
        for line in input.split("\n")
    ]
    # input = []
    # for line in f.readlines():
    # input.append(int(line))
    # input = [int(line) for line in f.readlines()]
    # input = [line for line in f.readlines()]

print(input)

# PART 1
solution_1 = 0

bla = {}
# calculate all distances?
for key1, key2 in itertools.combinations(input, 2):
    distance = (abs(key1.real - key2.real) + 1) * (abs(key1.imag - key2.imag) + 1)
    bla[(key1, key2)] = int(distance)

solution_1 = max(bla.values())

### SOLUTION 1
print("Part One : " + str(solution_1))

submit(solution_1, part="a", day=9, year=2025)

# PART 2
solution_2 = 0

coords = [(int(x.real), int(x.imag)) for x in input]
poly = Polygon(coords)

sorted_bla = sorted(bla.items(), key=lambda x: x[1], reverse=True)

for rectangle in sorted_bla:
    # print(rectangle)
    x1, y1 = int(rectangle[0][0].real), int(rectangle[0][0].imag)
    x2, y2 = int(rectangle[0][1].real), int(rectangle[0][1].imag)

    min_x, max_x = min(x1, x2), max(x1, x2)
    min_y, max_y = min(y1, y2), max(y1, y2)

    rect_corners = [(min_x, min_y), (max_x, min_y), (max_x, max_y), (min_x, max_y)]
    # print(rect_corners)
    rect = Polygon(rect_corners)
    if not poly.overlaps(rect):
        solution_2 = rectangle[1]
        break

### SOLUTION 2
print("Part Two : " + str(solution_2))

submit(solution_2, part="b", day=9, year=2025)
