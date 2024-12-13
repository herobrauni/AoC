# Advent of Code Year 2024 Day 13 solution
# Author = brauni
# Date = 2024-12-13

from collections import deque
import math
import sys
import functools
import re
import os
from aocd import submit
from aocd.models import Puzzle
puzzle = Puzzle(year=2024, day=13)

with open(os.getcwd() + "/2024/13/example.txt", 'r') as f:
    # with open(os.getcwd() + "/AoC_private/2024/13/input.txt", 'r') as f:
    input = f.read()
    input = input.split("\n\n")


@functools.cache
def lowest_cost(current, n, m, a, b, target, s):
    # print(current)
    if current in d and s >= d[current]:
        return 999999999999999999999999999999
    d[current] = s
    if n >= m:
        return 999999999999999999999999999999
    elif current.real > target.real or current.imag > target.imag:
        return 999999999999999999999999999999
    elif current == target:
        return s
    else:
        return min(lowest_cost(current+a, n+1, m, a, b, target, s+3), lowest_cost(current+b, n+1, m, a, b, target, s+1))


@functools.cache
def lowest_cost_queue(current, n, m, a, b, target, s):
    queue = deque()
    queue.append((current, n, m, s))
    while len(queue) > 0:
        q = queue.pop()
        current, n, m, s = q[0], q[1], q[2], q[3]
        if current in d and s >= d[current]:
            continue
        d[current] = s
        if current == target:
            print("hit with :", s)
            break
        else:
            queue.append((current+a, n+1, m, s+3))
            queue.append((current+b, n+1, m, s+1))


@functools.cache
def p2(current, a, b, n):
    if n >= 10000:
        return
    # if current in d and s >= d[current]:
    #     return
    if current.real % a.real == 0 and current.imag % a.imag == 0:
        if current.real // a.real == current.imag // a.imag:
            print("yay a", current, a)
    if current.real % b.real == 0 and current.imag % b.imag == 0:
        if current.real // b.real == current.imag // b.imag:
            print("yay b", current, b)
    p2(current-a, a, b, n+1)
    p2(current-b, a, b, n+1)

# # PART 1
# solution_1 = 0

# for i in input:
#     # i = input[0]
#     a, b = re.findall(r'Button [A|B]: X\+(\d+), Y\+(\d+)', i)
#     target = re.findall(r'Prize: X=(\d+), Y=(\d+)', i)
#     a, b = complex(int(a[0]), int(a[1])), complex(int(b[0]), int(b[1]))
#     target = complex(int(target[0][0]), int(target[0][1]))
#     d = {}
#     bla = lowest_cost(0j, 0, 200, a, b, target, 0)
#     # print(bla)
#     solution_1 += bla if bla != 999999999999999999999999999999 else 0


# # SOLUTION 1
# print("Part One : " + str(solution_1))

# submit(solution_1, part="a", day=13, year=2024)
# PART 2
solution_2 = 0
for i in input:
    # i = input[0]
    a, b = re.findall(r'Button [A|B]: X\+(\d+), Y\+(\d+)', i)
    target = re.findall(r'Prize: X=(\d+), Y=(\d+)', i)
    a, b = complex(int(a[0]), int(a[1])), complex(int(b[0]), int(b[1]))
    target = complex(int(target[0][0]), int(target[0][1]))
    target = target + (10000000000000+10000000000000j)
    d = {}
    bla = lowest_cost_queue(0j, 0, 100000, a, b, target, 0)
    print(bla)
    solution_2 += bla if bla != 999999999999999999999999999999 else 0


# SOLUTION 2
print("Part Two : " + str(solution_2))

# submit(solution_2, part="b", day=13, year=2024)


print(sys.getrecursionlimit())
sys.setrecursionlimit(999999999)
