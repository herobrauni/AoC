# Advent of code Year 2021 Day 24 solution
# Author = brauni
# Date = 2021-12-24
"https://adventofcode.com/2021/day/24"

import re
from collections import Counter
import copy
import os
import math

solution_1, solution_2 = 0, 0

# with open(os.getcwd() + "/2021/24/example.txt", 'r') as f:
with open(os.getcwd() + "/2021/24/input2.txt", 'r') as f:
    # input = f.read()
    # input = input.split("\n")
    # input = []
    # for line in f.readlines():
    # input.append(int(line))
    # input = [int(line) for line in f.readlines()]
    input = [line.strip() for line in f.readlines()]

# PART 0
input_formated = []
for line in input:
    line = line.split(" ")
    line = [str(x) for x in line]
    input_formated.append(line)

"""
print(input)
"""

# PART 1
number = 100000000000000

while number > 10000000000000:
    w, x, y, z = 0, 0, 0, 0
    i = 0
    number -= 1
    if "0" in str(number):
        continue
    n = [int(x) for x in list(str(number))]
    # print(number)
    # Number 1
    y = n[0]+1
    z = y

    # Number 2
    y = n[1]+9
    z = z*26+y

    # Number 3
    y = n[2]+11
    z = z*26+y

    # Number 4
    x = 0 if (z % 26)-13 == n[3] else 1
    y = 25*x+1
    z = (z//26)*y + ((n[3]+6)*x)

    # Number 5
    y = n[4]+6
    z = z*26+y

    # Number 6
    y = n[5]+13
    z = z*26+y

    # Number 7
    x = 0 if (z % 26)-14 == n[6] else 1
    y = 25*x+1
    z = z*y + ((n[6]+13)*x)

    # Number 8
    y = n[7]+5
    z = z*26+y

    # Number 9
    x = 0 if (z % 26)-8 == n[8] else 1
    y = 25*x+1
    z = z*y + ((n[8]+7)*x)

    # Number 10
    y = n[9]+2
    z = z*26+y

    # Number 11
    x = 0 if (z % 26)-9 == n[10] else 1
    y = 25*x+1
    z = (z//26)*y + ((n[10]+10)*x)

    # Number 12
    x = 0 if (z % 26)-11 == n[11] else 1
    y = 25*x+1
    z = (z//26)*y + ((n[11]+14)*x)

    # Number 13
    x = 0 if (z % 26)-6 == n[12] else 1
    y = 25*x+1
    z = (z//26)*y + ((n[12]+7)*x)

    # Number 14
    x = 0 if (z % 26)-5 == n[13] else 1
    y = 25*x+1
    z = (z//26)*y + ((n[13]+1)*x)

    if z == 0:
        solution_1 = number
        break
# print(helper)

# PART 2
# SOLUTIONS

print("Part One : " + str(solution_1) + "\nPart Two : " + str(solution_2))


number = 100000000000000

while number > 10000000000000:
    w, x, y, z = 0, 0, 0, 0
    i = 0
    number -= 1
    if "0" in str(number):
        continue
    n = [int(x) for x in list(str(number))]

n = [int(x) for x in list(str(5389))]
if n[-1] == n[-2]+1 == n[-3]+6 == n[-4]+4:
    print("".join([str(x) for x in n]))
