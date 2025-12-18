# Advent of Code Year 2024 Day 9 solution
# Author = brauni
# Date = 2024-12-09

import copy
import os
from aocd import submit
from aocd.models import Puzzle
puzzle = Puzzle(year=2024, day=9)

# with open(os.getcwd() + "/2024/09/example.txt", 'r') as f:
with open(os.getcwd() + "/AoC_private/2024/09/input.txt", 'r') as f:
    input = f.read()

print(input)

# PART 1
solution_1 = 0
g = []
space = False
c = 0
for i in range(len(input)):
    if space:
        for t in range(int(input[i])):
            g.append(["."])
    else:
        for t in range(int(input[i])):
            g.append([str(c)])
        c += 1
    space = not space
# f = [x for x in "".join(g)]
f = copy.deepcopy(g)
ff = [x for x in g if x != ["."]]
# z = re.finditer(r'\.', "".join(g))
for y in range(len(f)):
    f[y] = ff.pop() if f[y] == ["."] else f[y]

f = f[:-sum([1 for x in g if x == ["."]])]

for i, x in enumerate(f):
    solution_1 += i * int(x[0])

# SOLUTION 1
print("Part One : " + str(solution_1))

submit(solution_1, part="a", day=9, year=2024)


# PART 2
solution_2 = 0
g = []
space = False
c = 0
for i in range(len(input)):
    if space and int(input[i]) != 0:
        g.append(["."]*int(input[i]))
    elif int(input[i]) != 0:
        g.append([str(c)]*int(input[i]))
        c += 1
    space = not space

f = copy.deepcopy(g)
ff = [x for x in g if '.' not in x]
ff.reverse()
for y in range(len(ff)):
    for x in range(len(f)):
        if "." in f[x] and len(f[x]) >= len(ff[y]):
            if len(f[x]) == len(ff[y]):
                f[x] = ff[y]
            else:
                dif = len(f[x]) - len(ff[y])
                f[x] = ff[y]
                f.insert(x+1, ["."]*dif)
            f.reverse()
            for r in range(len(f)):
                if f[r] == ff[y]:
                    f[r] = ["."]*len(ff[y])
                    f.reverse()
                    break
            break
f = [x for xs in f for x in xs]
for i, x in enumerate(f):
    solution_2 += i * int(x) if x != "." else 0

# SOLUTION 2
print("Part Two : " + str(solution_2))

submit(solution_2, part="b", day=9, year=2024)
