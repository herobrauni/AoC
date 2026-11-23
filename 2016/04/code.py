# Advent of Code Year 2016 Day 4 solution
# Author = brauni
# Date = 2016-12-04

import re
import os
from aocd import submit
from aocd.models import Puzzle
from collections import Counter
puzzle = Puzzle(year=2016, day=4)


# with open(os.getcwd() + "/2016/04/example.txt", 'r') as f:
with open(os.getcwd() + "/AoC_private/2016/04/input.txt", 'r') as f:
    input = f.read()
    input = input.split("\n")
    # input = []
    # for line in f.readlines():
    # input.append(int(line))
    # input = [int(line) for line in f.readlines()]
    # input = [line for line in f.readlines()]

# split each line into name, sector and checksum
rooms = []
for line in input:
    if not line.strip():
        continue
    m = re.match(r"^([a-z-]+)-(\d+)\[([a-z]+)\]$", line.strip())
    if m:
        name, sector, checksum = m.group(1), int(m.group(2)), m.group(3)
        rooms.append((name, sector, checksum))

print(rooms)

# PART 1
solution_1 = 0

# get the most used letters in the name, ties are broken by alphabetical order. compare with checksum.
for name, sector, checksum in rooms:
    letters = Counter(name.replace("-", ""))
    most_common = sorted(letters.items(), key=lambda x: (-x[1], x[0]))
    most_common = "".join([x[0] for x in most_common[:5]])
    if most_common == checksum:
        solution_1 += sector

### SOLUTION 1
print("Part One : " + str(solution_1))

submit(solution_1, part="a", day=4, year=2016)



# PART 2
solution_2 = 0

# decrypt the name by shifting each letter by the sector number, wrapping around from z to a. dashes become spaces.
for name, sector, checksum in rooms:
    decrypted_name = ""
    for c in name:
        if c == "-":
            decrypted_name += " "
        else:
            decrypted_name += chr((ord(c) - ord("a") + sector) % 26 + ord("a"))
    if "north" in decrypted_name and "pole" in decrypted_name:
        solution_2 = sector
        break


### SOLUTION 2
print("Part Two : " + str(solution_2))

submit(solution_2, part="b", day=4, year=2016)
