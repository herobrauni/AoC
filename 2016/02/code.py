# Advent of Code Year 2016 Day 2 solution
# Author = brauni
# Date = 2016-12-02

import re
import os
from aocd import submit
from aocd.models import Puzzle
puzzle = Puzzle(year=2016, day=2)


# with open(os.getcwd() + "/2016/02/example.txt", 'r') as f:
with open(os.getcwd() + "/AoC_private/2016/02/input.txt", 'r') as f:
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

# 3x3 keypad, coordinates as imaginary numbers (real = column, imag = row)
keypad = {
    1: -1 - 1j, 2: 0 - 1j, 3: 1 - 1j,
    4: -1 + 0j, 5: 0 + 0j, 6: 1 + 0j,
    7: -1 + 1j, 8: 0 + 1j, 9: 1 + 1j,
}
lookup = {coord: num for num, coord in keypad.items()}

moves = {"U": -1j, "D": 1j, "L": -1, "R": 1}

position = 0 + 0j  # start on "5"
for line in input:
    line = line.strip()
    if not line:
        continue
    for move in line:
        new_position = position + moves[move]
        if new_position in lookup:
            position = new_position
    solution_1 += str(lookup[position])

solution_1 = int(solution_1)

### SOLUTION 1
print("Part One : " + str(solution_1))

submit(solution_1, part="a", day=2, year=2016)



# PART 2
solution_2 = 0

# Diamond-shaped keypad, coordinates as imaginary numbers (real = column, imag = row)
keypad_2 = {
    "1": 0 - 2j,
    "2": -1 - 1j, "3": 0 - 1j, "4": 1 - 1j,
    "5": -2 + 0j, "6": -1 + 0j, "7": 0 + 0j, "8": 1 + 0j, "9": 2 + 0j,
    "A": -1 + 1j, "B": 0 + 1j, "C": 1 + 1j,
    "D": 0 + 2j,
}
lookup_2 = {coord: key for key, coord in keypad_2.items()}

position = 0 + 0j  # start on "5"
solution_2 = ""
for line in input:
    line = line.strip()
    if not line:
        continue
    for move in line:
        new_position = position + moves[move]
        if new_position in lookup_2:
            position = new_position
    solution_2 += lookup_2[position]

### SOLUTION 2
print("Part Two : " + str(solution_2))

submit(solution_2, part="b", day=2, year=2016)
