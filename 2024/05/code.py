# Advent of Code Year 2024 Day 5 solution
# Author = brauni
# Date = 2024-12-05

import os

from aocd import submit
from aocd.models import Puzzle

puzzle = Puzzle(year=2024, day=5)


# with open(os.getcwd() + "/2024/05/example.txt", 'r') as f:
with open(os.getcwd() + "/AoC_private/2024/05/input.txt", "r") as f:
    input = f.read()
    rules = input.split("\n\n")[0]
    rules = rules.split("\n")
    commands = input.split("\n\n")[1]
    commands = commands.split("\n")
    # input = []
    # for line in f.readlines():
    # input.append(int(line))
    # input = [int(line) for line in f.readlines()]
    # input = [line for line in f.readlines()]

print(rules)


# PART 1
solution_1 = 0
r = {}
bla = []
for line in rules:
    if line != "":
        line = line.split("|")
        x = line[0]
        y = line[1]
        if x in r.keys():
            r[x].append(y)
        else:
            r[x] = [y]

for line in commands:
    line = line.split(",")
    # print(line)
    done = []
    fail = False
    for x in line:
        if len(done) == 0:
            done.append(x)
        else:
            if x not in r.keys():
                done.append(x)
                continue
            for y in r[x]:
                if y in done:
                    print("failed for ", line)
                    fail = True
                    break
            else:
                done.append(x)
    else:
        if not fail:
            print("yes: ", line)
            bla.append(line)
            length = len(line)
            m = length // 2
            solution_1 += int(line[m])


# SOLUTION 1
print("Part One : " + str(solution_1))

submit(solution_1, part="a", day=5, year=2024)


# PART 2
solution_2 = 0
for line in commands:
    line = line.split(",")
    if line in bla:
        continue
    done = []
    z = 0
    while len(line) > 0:
        for x in line:
            if x == line[z]:
                continue
            elif x not in r.keys():
                continue
            elif line[z] in r[x]:
                z += 1
                break
        else:
            t = line.pop(z)
            done.append(t)
            z = 0
    solution_2 += int(done[len(done) // 2])


# SOLUTION 2
print("Part Two : " + str(solution_2))

submit(solution_2, part="b", day=5, year=2024)
