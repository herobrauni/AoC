# Advent of code Year 2023 Day 13 solution
# Author = brauni
# Date = 2023-12-13
"https://adventofcode.com/2023/day/13"

import re
from collections import Counter
import copy
import os
import math
import numpy as np

solution_1, solution_2 = 0, 0

with open(os.getcwd() + "/AoC_private/2023/13/input.txt", "r") as f:
    # with open(os.getcwd() + "/2023/13/example.txt", "r") as f:
    input = f.read()
    input = input.split("\n\n")

# PART 0


print(input)
input_clean = []
for line in input:
    l = re.search(r"\n", line)
    n = len(re.findall(r"\n", line)) + 1
    x = np.array([x for x in line.replace("\n", "")])
    x = x.reshape(n, l.start())
    input_clean.append(x)


# PART 1
print(input_clean[0])


def mirror_that(line, already_found):
    verts, horz = already_found[0], already_found[1]
    for mirror in range(1, len(line[0])):
        l = len(line[0])
        a, b = line[:, 0:mirror], line[:, mirror:]
        p = len(a[0]) if len(a[0]) <= len(b[0]) else len(b[0])
        for z in range(p):
            z1 = None if z == 0 else -z
            if not np.array_equal(a[:, -1 - z : z1], b[:, z : z + 1]):
                break
        else:
            if verts != mirror:
                verts = mirror
                horz = 0
                break

    else:
        for mirror in range(1, len(line)):
            aa, bb = line[0:mirror, :], line[mirror:, :]
            pp = len(aa) if len(aa) <= len(bb) else len(bb)
            for z in range(pp):
                z1 = None if z == 0 else -z
                # if not np.array_equal(aa[:, -1 - z : z1], bb[:, z : z + 1]):
                if not np.array_equal(aa[-1 - z : z1, :], bb[z : z + 1, :]):
                    break
            else:
                if horz != mirror:
                    verts = 0
                    horz = mirror
                    break
    return verts, horz


res = {}
for n, line in enumerate(input_clean):
    res[n] = mirror_that(line, (0, 0))

# line = input_clean[0]
n = 0
res_p2 = copy.deepcopy(res)
for n, line in enumerate(input_clean):
    for i in np.ndindex(*line.shape):
        line_new = copy.deepcopy(line)
        line_new[i] = "#" if line[i] == "." else "."
        # print(line_new)
        t = mirror_that(line_new, res[n])
        if t != (0, 0) and t != res[n]:
            print(t)
            res_p2[n] = t
            break


solution_1 = sum([res[x][0] for x in res]) + sum([res[x][1] * 100 for x in res])
solution_2 = sum([res_p2[x][0] for x in res]) + sum([res_p2[x][1] * 100 for x in res])

# PART 2


# SOLUTIONS

print("Part One : " + str(solution_1) + "\nPart Two : " + str(solution_2))
