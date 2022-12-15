# Advent of code Year 2022 Day 15 solution
# Author = brauni
# Date = 2022-12-15
"https://adventofcode.com/2022/day/15"

import re
from collections import Counter
import copy
import os
import math
import numpy as np

solution_1, solution_2 = 0, 0

# with open(os.getcwd() + "/2022/15/example.txt", 'r') as f:
with open(os.getcwd() + "/2022/15/input.txt", 'r') as f:    
    input = f.read()
    input = input.split("\n")


# PART 0
input_clean = []
for line in input:
    input_clean.append([int(line.split()[x].strip("xy=,:")) for x in [2, 3, 8, 9]])

sensors = set()
beacons = set()
blocked = set()
sensor_dict = {}


def manh(x1, y1, x2, y2):
    return abs(x1-x2) + abs(y1-y2)


# PART 1
row = 2000000
for x in input_clean:
    sensor = x[0] + x[1] * 1j
    beacon = x[2] + x[3] * 1j
    sensors.add(sensor)
    beacons.add(beacon)
    dist = manh(x[0], x[1], x[2], x[3])
    start_p2 = [x[0]+dist+1, x[1]]
    sensor_dict[sensor] = [x[0], x[1], x[2], x[3], dist, start_p2]
    off = 0
    while manh(x[0], x[1], x[0]+off, row) <= dist:
        blocked.add(x[0]+off + row*1j)
        off = off + 1
    off = 0
    while manh(x[0], x[1], x[0]-off, row) <= dist:
        blocked.add(x[0]-off + row*1j)
        off = off + 1

solution_1 = sum([1 for x in blocked if x.imag == row and x not in beacons and x not in sensors])

borders = Counter()
asddas = 1
for key in sensor_dict:
    c = tuple(sensor_dict[key][5])
    for i in range(sensor_dict[key][4]+1):
        borders[c] += 1
        c = c[0]-1, c[1]-1
    for i in range(sensor_dict[key][4]+1):
        borders[c] += 1
        c = c[0]-1, c[1]+1
    for i in range(sensor_dict[key][4]+1):
        borders[c] += 1
        c = c[0]+1, c[1]+1
    for i in range(sensor_dict[key][4]+1):
        borders[c] += 1
        c = c[0]+1, c[1]-1
    print(asddas)
    asddas += 1


x = lambda a: a[0]*4000000 + a[1]

solution_2 = x(borders.most_common(1)[0][0])

print("Part One : " + str(solution_1) + "\nPart Two : " + str(solution_2))
