# Advent of code Year 2022 Day 11 solution
# Author = brauni
# Date = 2022-12-11
"https://adventofcode.com/2022/day/11"

import re
from collections import Counter
import copy
import os
import math

solution_1, solution_2 = 0, 0

# with open(os.getcwd() + "/2022/11/example.txt", 'r') as f:
with open(os.getcwd() + "/2022/11/input.txt", 'r') as f:
    input = f.read()
    input = input.split("\n\n")
    input = [x.split("\n") for x in input]
    # input = []
    # for line in f.readlines():
    # input.append(int(line))
    # input = [int(line) for line in f.readlines()]
    # input = [line for line in f.readlines()]

# PART 0

print(input)

divs = [int(input[x][3][21:]) for x in range(len(input))]

monkeys = {}
for i in range(len(input)):
    monkeys[i] = {
        "items": [int(x) for x in input[i][1][18:].split(",")],
        "operation": input[i][2][19:],
        "div": int(input[i][3][21:]),
        "true": int(input[i][4][29:]),
        "false": int(input[i][5][30:]),
        "counter": 0
    }

for i in range(20):
    # print(i)
    for j in range(len(monkeys)):
        k = len(monkeys[j]["items"])
        for h in range(k):
            monkeys[j]["counter"] += 1
            t = monkeys[j]["items"].pop(0)
            match monkeys[j]["operation"].split()[1]:
                case "+": t = t + int(monkeys[j]["operation"].split()[2]) if monkeys[j]["operation"].split()[2] != "old" else t + t
                case "*": t = t * int(monkeys[j]["operation"].split()[2]) if monkeys[j]["operation"].split()[2] != "old" else t * t
            t = t//3
            if t % divs[j] == 0:
                monkeys[monkeys[j]["true"]]["items"].append(t)
            else:
                monkeys[monkeys[j]["false"]]["items"].append(t)
solution_1 = [monkeys[x]["counter"] for x in monkeys]
solution_1.sort(reverse=True)
solution_1 = solution_1[0]*solution_1[1]


# PART 2
monkeys = {}
for i in range(len(input)):
    monkeys[i] = {
        "items": [[int(x) % div for div in divs] for x in input[i][1][18:].split(",")],
        "operation": input[i][2][19:],
        "div": int(input[i][3][21:]),
        "true": int(input[i][4][29:]),
        "false": int(input[i][5][30:]),
        "counter": 0
    }
for i in range(10000):
    # print(i)
    for j in range(len(monkeys)):
        k = len(monkeys[j]["items"])
        for h in range(k):
            monkeys[j]["counter"] += 1
            t = monkeys[j]["items"].pop(0)
            for z in range(len(t)):
                match monkeys[j]["operation"].split()[1]:
                    # case "+": t = t + int(monkeys[j]["operation"].split()[2]) if monkeys[j]["operation"].split()[2] != "old" else t + t
                    case "+":
                        t[z] = (t[z] + int(monkeys[j]["operation"].split()[2])) % divs[z]
                    # case "*": t = t * int(monkeys[j]["operation"].split()[2]) if monkeys[j]["operation"].split()[2] != "old" else t * t
                    case "*":
                        t[z] = (t[z] * int(monkeys[j]["operation"].split()[2])
                                ) % divs[z] if monkeys[j]["operation"].split()[2] != "old" else (t[z] ** 2) % divs[z]

            if t[j] == 0:
                monkeys[monkeys[j]["true"]]["items"].append(t)
            else:
                monkeys[monkeys[j]["false"]]["items"].append(t)


solution_2 = [monkeys[x]["counter"] for x in monkeys]
solution_2.sort(reverse=True)
solution_2 = solution_2[0]*solution_2[1]

# SOLUTIONS
print("Part One : " + str(solution_1) + "\nPart Two : " + str(solution_2))
