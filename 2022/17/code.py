# Advent of code Year 2022 Day 17 solution
# Author = brauni
# Date = 2022-12-27
"https://adventofcode.com/2022/day/17"

import re
from collections import Counter, deque
import copy
import os
import math
import numpy as np


solution_1, solution_2=0, 0

# with open(os.getcwd() + "/2022/17/example.txt", 'r') as f:
with open(os.getcwd() + "/2022/17/input.txt", 'r') as f:
    input = f.read()
    # input = input.split("\n")
    # input = []
    # for line in f.readlines():
        # input.append(int(line))
    # input = [int(line) for line in f.readlines()]
    # input = [line for line in f.readlines()]

# PART 0


print(input)


def rotate(a, h, direction):
    t = copy.deepcopy(a)
    blub = copy.deepcopy(grid)
    if direction == ">":
        if any([True for x in t if x[-1] !=0]): return a
        for x in t: x.rotate(1)
    elif direction == "<":
        if any([True for x in t if x[0] !=0]): return a
        for x in t: x.rotate(-1)
    for i in range(4):
        blub[h+i] = np.add(t[3-i],grid[h+i])
        if any([True for x in blub[h+i] if x > 1]):
            return a
    else:
        return t

def collision(a,h):
    blub = copy.deepcopy(grid)
    for i in range(4):
        blub[h+i] = np.add(a[3-i],grid[h+i])
        if any([True for x in blub[h+i] if x > 1]):
            return True
    else:
        return False

def place(a,h):
    for i in range(4):
        grid[h+i] = np.add(a[3-i],grid[h+i])

# PART 1
runs = 2022

h = 1
grid = np.zeros(((runs)*7*4), dtype=int).reshape(runs*4,7)
grid[0] = [1,1,1,1,1,1,1]

line = [deque([0,0,0,0,0,0,0]),deque([0,0,0,0,0,0,0]),deque([0,0,0,0,0,0,0]),deque([0,0,1,1,1,1,0])]
cross = [deque([0,0,0,0,0,0,0]),deque([0,0,0,1,0,0,0]),deque([0,0,1,1,1,0,0]),deque([0,0,0,1,0,0,0])]
l = [deque([0,0,0,0,0,0,0]),deque([0,0,0,0,1,0,0]),deque([0,0,0,0,1,0,0]),deque([0,0,1,1,1,0,0])]
vert = [deque([0,0,1,0,0,0,0]),deque([0,0,1,0,0,0,0]),deque([0,0,1,0,0,0,0]),deque([0,0,1,0,0,0,0])]
cube = [deque([0,0,0,0,0,0,0]),deque([0,0,0,0,0,0,0]),deque([0,0,1,1,0,0,0]),deque([0,0,1,1,0,0,0])]

d_c = 0

for i in range(runs):
    if i % 5 == 0 :
        form = line
    elif i % 5 == 1 :
        form = cross
    elif i % 5 == 2 :
        form = l
    elif i % 5 == 3 :
        form = vert
    elif i % 5 == 4 :
        form = cube
    h = h + 3
    while not collision(form, h):
        # print(h, form)
        form = rotate(form, h, input[d_c % len(input)])
        d_c += 1
        h -= 1
    place(form, h+1)
    while sum(grid[h])>0:
        h+=1
solution_1 = h-1

# # PART 2

def bbb(runs):
    bla = set()
    # runs = 1879
    h = 1

    grid = np.zeros(((runs)*7*4), dtype=int).reshape(runs*4,7)
    grid[0] = [1,1,1,1,1,1,1]

    line = [deque([0,0,0,0,0,0,0]),deque([0,0,0,0,0,0,0]),deque([0,0,0,0,0,0,0]),deque([0,0,1,1,1,1,0])]
    cross = [deque([0,0,0,0,0,0,0]),deque([0,0,0,1,0,0,0]),deque([0,0,1,1,1,0,0]),deque([0,0,0,1,0,0,0])]
    l = [deque([0,0,0,0,0,0,0]),deque([0,0,0,0,1,0,0]),deque([0,0,0,0,1,0,0]),deque([0,0,1,1,1,0,0])]
    vert = [deque([0,0,1,0,0,0,0]),deque([0,0,1,0,0,0,0]),deque([0,0,1,0,0,0,0]),deque([0,0,1,0,0,0,0])]
    cube = [deque([0,0,0,0,0,0,0]),deque([0,0,0,0,0,0,0]),deque([0,0,1,1,0,0,0]),deque([0,0,1,1,0,0,0])]

    d_c = 0
    bla = []

    for i in range(runs):
        if i % 5 == 0 :
            form = line
        elif i % 5 == 1 :
            form = cross
        elif i % 5 == 2 :
            form = l
        elif i % 5 == 3 :
            form = vert
        elif i % 5 == 4 :
            form = cube
        h = h + 3
        while not collision(form, h):
            if d_c % len(input) == 0 and i%5 == 4:
                print(i, h, i%5, grid[h],grid[h-1])
                if i%5 == 0:
                    bla.append([i,h])
            # print(h, form)
            form = rotate(form, h, input[d_c % len(input)])
            d_c += 1
            h -= 1
        place(form, h+1)
        while sum(grid[h])>0:
            h+=1
    solution_2 = h -1
    return solution_2, runs


# SOLUTIONS

# for i in range(30):
#     print(' '.join(["." if x == 0 else "#" for x in grid[30-i-1]]))

print("Part One : "  + str(solution_1) + "\nPart Two : " + str(solution_2) + " " +  str(runs))


# grid[14]


bbb(2022)