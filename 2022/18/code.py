# Advent of code Year 2022 Day 18 solution
# Author = brauni
# Date = 2022-12-27
"https://adventofcode.com/2022/day/18"

import re
from collections import Counter
import copy
import os
import math
import itertools as it
import numpy as np

solution_1, solution_2=0, 0

# with open(os.getcwd() + "/2022/18/example.txt", 'r') as f:
with open(os.getcwd() + "/2022/18/input.txt", 'r') as f:
    input = f.read()
    input = input.split("\n")
    # input = []
    # for line in f.readlines():
        # input.append(int(line))
    # input = [int(line) for line in f.readlines()]
    # input = [line for line in f.readlines()]

# PART 0


print(input)
ic = []
for line in input:
    i = [int(x) for x in line.split(",")]
    ic.append(i)

# PART 1
for i in range(len(ic)):
    x = 6
    if [ic[i][0]+1,ic[i][1],ic[i][2]] in ic: x-=1
    if [ic[i][0],ic[i][1]+1,ic[i][2]] in ic: x-=1
    if [ic[i][0],ic[i][1],ic[i][2]+1] in ic: x-=1
    if [ic[i][0]-1,ic[i][1],ic[i][2]] in ic: x-=1
    if [ic[i][0],ic[i][1]-1,ic[i][2]] in ic: x-=1
    if [ic[i][0],ic[i][1],ic[i][2]-1] in ic: x-=1
    # for j in range(len(ic[i])):
    #     if ic[i][j]+1 in [x[j] for x in ic]: x -= 1
    #     if ic[i][j]-1 in [x[j] for x in ic]: x -= 1
    solution_1 += x

# PART 2
xm,ym,zm = range(1,max([int(x[0]) for x in ic])),range(1,max([int(x[1]) for x in ic])),range(1,max([int(x[2]) for x in ic]))
a = [xm,ym,zm]
t = list(it.product(*a))

tp = [np.array(x) for x in t if list(x) not in ic]

bla = []

ic_np = [np.array(x) for x in ic]

left = np.array([-1,0,0])
right = np.array([1,0,0])
down = np.array([0,-1,0])
up = np.array([0,1,0])
back = np.array([0,0,1])
forward = np.array([0,0,-1])

# for line in tp:
#     while True:
#         for x in [left, right, down, up, back, forward]:
#             if list(np.add(line, x)) in ic: continue
#         else:
#             bla.append(line)
#             break


def check_if_surface(a, ic):
    print(a)
    if any([a[0] not in xm, a[1] not in ym, a[2] not in zm]):
        return True
    else:
        return any([check_if_surface([a[0]+1,a[1],a[2]],ic)])

check_if_surface([2,2,5],ic)

def istrapped(a):
    if all([
    [a[0]+1,a[1],a[2]] in ic,
    [a[0],a[1]+1,a[2]] in ic,
    [a[0],a[1],a[2]+1] in ic,
    [a[0]-1,a[1],a[2]] in ic,
    [a[0],a[1]-1,a[2]] in ic,
    [a[0],a[1],a[2]-1] in ic]): return True


left = np.array([-1,0,0])
right = np.array([1,0,0])
down = np.array([0,-1,0])
up = np.array([0,1,0])
back = np.array([0,0,1])
forward = np.array([0,0,-1])
def en(a, empN):
    abc = -1
    t = []
    for x in [left, right, down, up, back, forward]:
        t.append(list(np.add(a, x)))
    if all([True if tuple(x) in empN else False for x in t]):
        return
    while abc < len(empN):
        abc = len(empN)
        for x in [left, right, down, up, back, forward]:
            if list(np.add(a, x)) not in ic \
            and tuple(np.add(a, x)) not in empN \
            and all([list(np.add(a, x))[0] in xm,list(np.add(a, x))[1] in ym,list(np.add(a, x))[2] in zm]): 
                empN.add(tuple(np.add(a, x)))
                # empN.update(en(list(np.add(a, x)), empN))
    # empN = [en(x, empN) for x in empN]
    return empN

blub = []

for ty in tp:
    empN = en(ty, set())
    # [x for x in empN]
    if all([[x[0] in xm, x[1] in ym, x[2]] in zm for x in empN]): 
        blub.append(list(ty))
adsas = 0
for i in range(len(blub)):
    x = 6
    if [blub[i][0]+1,blub[i][1],blub[i][2]] in blub + ic: x-=1
    if [blub[i][0],blub[i][1]+1,blub[i][2]] in blub + ic: x-=1
    if [blub[i][0],blub[i][1],blub[i][2]+1] in blub + ic: x-=1
    if [blub[i][0]-1,blub[i][1],blub[i][2]] in blub + ic: x-=1
    if [blub[i][0],blub[i][1]-1,blub[i][2]] in blub + ic: x-=1
    if [blub[i][0],blub[i][1],blub[i][2]-1] in blub + ic: x-=1
    adsas += x

solution_2 = solution_1 - len(blub)*6

# SOLUTIONS

print("Part One : "  + str(solution_1) + "\nPart Two : " + str(solution_2))