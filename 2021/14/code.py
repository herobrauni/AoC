# Advent of code Year 2021 Day 14 solution
# Author = brauni
# Date = 2021-12-14
"https://adventofcode.com/2021/day/14"

import re
from collections import Counter
import copy
import os
import math

solution_1, solution_2 = 0, 0

# with open(os.getcwd() + "\\2021\\14\\example.txt", 'r') as f:
with open(os.getcwd() + "\\2021\\14\\input.txt", 'r') as f:
    input = f.read()
    input = input.split("\n\n")


# PART 0
# Split input into the starting Polymer and the rules
start = input[0]
pair_rules = {}
for line in input[1].split("\n"):
    line = line.split(" -> ")
    pair_rules[line[0]] = line[1]

# PART 1
# Create starting Counter for the polymer, we count Pairs for evolution and single Chars for the solution
test = []
for i in range(1, len(start)):
    test.append(start[i-1:i+1])

c = Counter(test) + Counter(start)


# Rotate the counter each evolution step
# we add the new pairs to c_new and update the amount of each char
def poly(c, pair_rules, n):
    for i in range(n):
        print("round ", i+1)
        keys_static = list(c.keys())
        c_new = Counter()
        for keys in keys_static:
            if len(keys) == 1:
                c_new[keys] += c[keys]
            if len(keys) == 2 and c[keys] != 0:
                # print("Pair: ", keys)
                if keys in pair_rules:
                    x = keys[0]+pair_rules[keys]
                    y = pair_rules[keys] + keys[1]
                    c_new[x] += c[keys]
                    c_new[y] += c[keys]
                    c_new[pair_rules[keys]] += c[keys]
        c = c_new
    return c


# Get the counters for both parts (evolution steps 10 and 40)
# count only single char entries in the Counters
# subtract least used letter from most common letter
c_p1, c_p2 = poly(c, pair_rules, 10), poly(c, pair_rules, 40)
final_p1, final_p2 = [c_p1[x] for x in c_p1 if len(
    x) == 1], [c_p2[x] for x in c_p2 if len(x) == 1]
solution_1, solution_2 = max(
    final_p1) - min(final_p1), max(final_p2) - min(final_p2)

# SOLUTIONS
print("Part One : " + str(solution_1) + "\nPart Two : " + str(solution_2))
