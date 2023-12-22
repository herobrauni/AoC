# Advent of code Year 2023 Day 20 solution
# Author = brauni
# Date = 2023-12-20
"https://adventofcode.com/2023/day/20"

import re
from collections import Counter
import copy
import os
import math

solution_1, solution_2 = 0, 0

with open(os.getcwd() + "/AoC_private/2023/20/input.txt", "r") as f:
    # with open(os.getcwd() + "/2023/20/example.txt", "r") as f:
    input = f.read()
    input = input.split("\n")

# PART 0
print(input)
t = {}
for line in input:
    mod, tar = line.split(" -> ")
    typ = "flip" if mod[0] == "%" else "conj"
    if typ == "conj":
        if mod not in ["broadcaster", "output"]:
            mod = mod[1:]
            t[mod] = {}
            t[mod]["typ"] = typ
            t[mod]["out"] = tar.split(", ")
            t[mod]["state"] = {}
for line in input:
    mod, tar = line.split(" -> ")
    typ = "flip" if mod[0] == "%" else "conj"
    if mod == "broadcaster":
        t[mod] = {}
        t[mod]["typ"] = 0
        t[mod]["out"] = tar.split(", ")
        for out in t[mod]["out"]:
            if out in [x for x in t if t[x]["typ"] == "conj"]:
                t[out]["state"][mod] = 0
    elif typ == "flip":
        mod = mod[1:]
        t[mod] = {}
        t[mod]["typ"] = typ
        t[mod]["out"] = tar.split(", ")
        t[mod]["state"] = 0 if typ == "flip" else []
        for out in t[mod]["out"]:
            if out in [x for x in t if t[x]["typ"] == "conj"]:
                t[out]["state"][mod] = 0
    elif typ == "conj":
        mod = mod[1:]
        for out in t[mod]["out"]:
            if out in [x for x in t if t[x]["typ"] == "conj"]:
                t[out]["state"][mod] = 0
for line in input:
    mod, tar = line.split(" -> ")
    outs = tar.split(", ")
    for out in outs:
        if out not in t:
            t[out] = {}
            t[out]["typ"] = "end"
            t[out]["out"] = []
# for x in t.items():
#     print(x)


# PART 1
def impuls(cur, imp, t, looking_for=[], part=1):
    queue = [(cur, imp)]

    high = 0
    low = 0
    while queue:
        cur, imp = queue.pop(0)
        if imp == 0:
            low += 1
        if imp == 1:
            high += 1

        if part == 2:
            if cur == looking_for[0] and imp == looking_for[1]:
                return False, t
        if t[cur]["typ"] == 0:
            imp = 0
            for dest in t[cur]["out"]:
                if t[dest]["typ"] == "conj":
                    t[dest]["state"][cur] = imp
                queue.append((dest, imp))
        elif t[cur]["typ"] == "flip":
            if imp == 1:
                continue
            else:
                if t[cur]["state"] == 0:
                    t[cur]["state"] = 1
                    imp = 1
                elif t[cur]["state"] == 1:
                    t[cur]["state"] = 0
                    imp = 0
                for dest in t[cur]["out"]:
                    if t[dest]["typ"] == "conj":
                        t[dest]["state"][cur] = imp
                    queue.append((dest, imp))
        elif t[cur]["typ"] == "conj":
            if all([True if x == 1 else False for x in t[cur]["state"].values()]):
                imp = 0
            else:
                imp = 1
            for dest in t[cur]["out"]:
                if t[dest]["typ"] == "conj":
                    t[dest]["state"][cur] = imp
                queue.append((dest, imp))
    if part == 1:
        return high, low, t
    if part == 2:
        return (True, t)


high, low = 0, 0
t1 = copy.deepcopy(t)
for i in range(1000):
    h, l, t1 = impuls("broadcaster", 0, t1)
    high += h
    low += l
solution_1 = high * low

p2 = {"dt": 0, "qs": 0, "ts": 0, "js": 0}
for x in p2:
    i = 0
    t2 = copy.deepcopy(t)
    res = (True, t2)
    while res[0]:
        res = impuls("broadcaster", 0, res[1], (x, 0), 2)
        i += 1
    p2[x] = i

solution_2 = math.lcm(*p2.values())

# SOLUTIONS

print("Part One : " + str(solution_1) + "\nPart Two : " + str(solution_2))
