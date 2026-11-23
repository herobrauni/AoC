# Advent of Code Year 2016 Day 5 solution
# Author = brauni
# Date = 2016-12-05

import re
import os
from aocd import submit
from aocd.models import Puzzle
import hashlib
puzzle = Puzzle(year=2016, day=5)


# with open(os.getcwd() + "/2016/05/example.txt", 'r') as f:
with open(os.getcwd() + "/AoC_private/2016/05/input.txt", 'r') as f:
    input = f.read()
    input = input.split("\n")
    # input = []
    # for line in f.readlines():
    # input.append(int(line))
    # input = [int(line) for line in f.readlines()]
    # input = [line for line in f.readlines()]

# input[0] = 'abc'
print(input)

# PART 1
solution_1 = list()
bla = 0
hash = ""
for i in range(8):
    while hash[:5] != "00000":
        hash = hashlib.md5((input[0] + str(bla)).encode()).hexdigest()
        bla += 1
    print(hash)
    solution_1.append(hash[5])
    bla += 1
    hash = ""

### SOLUTION 1
solution_1 = ''.join(solution_1)
print("Part One : " + str(solution_1))

# submit(solution_1, part="a", day=5, year=2016)



# PART 2
solution_2 = [""] * 8
bla = 0
while "" in solution_2:
    hash = hashlib.md5((input[0] + str(bla)).encode()).hexdigest()
    if hash[:5] == "00000":
        pos = hash[5]
        if pos.isdigit() and int(pos) < 8 and solution_2[int(pos)] == "":
            solution_2[int(pos)] = hash[6]
            print("".join(solution_2))
    bla += 1



### SOLUTION 2
solution_2 = ''.join(solution_2)
print("Part Two : " + str(solution_2))

# submit(solution_2, part="b", day=5, year=2016)
