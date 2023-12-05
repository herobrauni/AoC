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
def run(runs, grid):
    h = 1

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
            # print(h, form)
            form = rotate(form, h, input[d_c % len(input)])
            d_c += 1
            h -= 1
            if d_c % len(input) == 0 : #and i%5 == 4
                print(i, h, i%5, grid[h-3],grid[h-2],grid[h-1], grid[h])
                bla.append([i, h, i%5, tuple(grid[h-5]),tuple(grid[h-4]),tuple(grid[h-3]),tuple(grid[h-2]),tuple(grid[h-1]),tuple(grid[h])])
        place(form, h+1)

        while sum(grid[h])>0:
            h+=1
    solution_1 = h-1
    return solution_1, bla

# # PART 2
runs = 10000
grid = np.zeros(((runs)*7*4), dtype=int).reshape(runs*4,7)
grid[0] = [1,1,1,1,1,1,1]

r,b = run(runs, grid)

test = [tuple(x[2:]) for x in b]

c = list(Counter(test).most_common(1))[0][0]

b = [x[:3] for x in b if tuple(x[2:]) == c]

all_runs = 1000000000000 - b[0][0]

diff_i = b[1][0]-b[0][0]
diff_h = b[1][1]-b[0][1]
rest_ende = all_runs % diff_i
full_runs = all_runs // diff_i

r2 = b[0][0]
grid = np.zeros(((r2)*7*4), dtype=int).reshape(r2*4,7)
grid[0] = [1,1,1,1,1,1,1]
start = run(r2, grid)

grid = np.zeros(((r2)*7*4), dtype=int).reshape(r2*4,7)
grid[0] = [1,1,1,1,1,1,1]
end = run(b[0][0] + rest_ende, grid)
ende = end[0]-start[0]

z = start[0] + full_runs * diff_h + ende

print(z)