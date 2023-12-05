# Advent of code Year 2022 Day 19 solution
# Author = brauni
# Date = 2022-12-27
"https://adventofcode.com/2022/day/19"

import re
from collections import Counter
import copy
import os
import math
from operator import add, sub
import itertools, functools

solution_1, solution_2 = 0, 1

# with open(os.getcwd() + "/2022/19/example.txt", 'r') as f:
with open(os.getcwd() + "/AoC_private/2022/19/input.txt", "r") as f:
    input = f.read()
    input = input.split("\n")
    # input = []
    # for line in f.readlines():
    # input.append(int(line))
    # input = [int(line) for line in f.readlines()]
    # input = [line for line in f.readlines()]

# PART 0


print(input)


# PART 1
ic = []
# ic.append([])
for x, line in enumerate(input):
    line = line.split()
    ic.append([])
    ic[x] = []
    ic[x].append(int(line[6]))
    ic[x].append(int(line[12]))
    ic[x].append((int(line[18]), int(line[21])))
    ic[x].append((int(line[27]), int(line[30])))


def build_robot(type, resources, robots, bp):
    match type:
        case "ore":
            if resources[0] < bp[0]:
                return resources, robots
            else:
                return list(map(sub, resources, [bp[0], 0, 0, 0])), list(
                    map(add, robots, [1, 0, 0, 0])
                )
        case "clay":
            if resources[0] < bp[1]:
                return resources, robots
            else:
                return list(map(sub, resources, [bp[1], 0, 0, 0])), list(
                    map(add, robots, [0, 1, 0, 0])
                )
        case "obs":
            if resources[0] < bp[2][0] or resources[1] < bp[2][1]:
                return resources, robots
            else:
                return list(map(sub, resources, [bp[2][0], bp[2][1], 0, 0])), list(
                    map(add, robots, [0, 0, 1, 0])
                )
        case "geode":
            if resources[0] < bp[3][0] or resources[2] < bp[3][1]:
                return resources, robots
            else:
                return list(map(sub, resources, [bp[3][0], 0, bp[3][1], 0])), list(
                    map(add, robots, [0, 0, 0, 1])
                )


def build_robot_no_check(type, resources, robots, bp):
    match type:
        case "ore":
            return list(map(sub, resources, [bp[0], 0, 0, 0])), list(
                map(add, robots, [1, 0, 0, 0])
            )
        case "clay":
            return list(map(sub, resources, [bp[1], 0, 0, 0])), list(
                map(add, robots, [0, 1, 0, 0])
            )
        case "obs":
            return list(map(sub, resources, [bp[2][0], bp[2][1], 0, 0])), list(
                map(add, robots, [0, 0, 1, 0])
            )
        case "geode":
            return list(map(sub, resources, [bp[3][0], 0, bp[3][1], 0])), list(
                map(add, robots, [0, 0, 0, 1])
            )


# @functools.cache
def fml(resources, robots, time, bp):
    # print(time)
    global d
    global state
    if (
        tuple(
            (
                resources[0],
                resources[1],
                resources[2],
                resources[3],
                robots[0],
                robots[1],
                robots[2],
                robots[3],
                time,
            )
        )
    ) in state:
        return
    if time >= 25:
        return
    if d[time][3] > resources[3]:
        return
    d[time] = resources if resources[3] >= d[time][3] else d[time]
    if resources[0] >= bp[3][0] and resources[2] >= bp[3][1]:
        fml(
            list(
                map(
                    add, build_robot_no_check("geode", resources, robots, bp)[0], robots
                )
            ),
            build_robot_no_check("geode", resources, robots, bp)[1],
            time + 1,
            bp,
        )
        # print("GEODE ROBOT BUILD")
        return
    if resources[0] >= bp[2][0] and resources[1] >= bp[2][1]:
        fml(
            list(
                map(add, build_robot_no_check("obs", resources, robots, bp)[0], robots)
            ),
            build_robot_no_check("obs", resources, robots, bp)[1],
            time + 1,
            bp,
        )
    if resources[0] >= bp[1]:
        fml(
            list(
                map(add, build_robot_no_check("clay", resources, robots, bp)[0], robots)
            ),
            build_robot_no_check("clay", resources, robots, bp)[1],
            time + 1,
            bp,
        )
        # print("CLAY ROBOT BUILD")

    if resources[0] >= bp[0]:
        fml(
            list(
                map(add, build_robot_no_check("ore", resources, robots, bp)[0], robots)
            ),
            build_robot_no_check("ore", resources, robots, bp)[1],
            time + 1,
            bp,
        )
    fml(list(map(add, resources, robots)), robots, time + 1, bp)
    state.add(
        (
            tuple(
                (
                    resources[0],
                    resources[1],
                    resources[2],
                    resources[3],
                    robots[0],
                    robots[1],
                    robots[2],
                    robots[3],
                    time,
                )
            )
        )
    )
    return


def fml_p2(resources, robots, time, bp):
    # print(time)
    global d
    global state
    if (
        tuple(
            (
                resources[0],
                resources[1],
                resources[2],
                resources[3],
                robots[0],
                robots[1],
                robots[2],
                robots[3],
                time,
            )
        )
    ) in state:
        return
    if time >= 33:
        return
    if d[time][3] - 5 > resources[3]:
        return
    d[time] = resources if resources[3] >= d[time][3] else d[time]
    if resources[0] >= bp[3][0] and resources[2] >= bp[3][1]:
        fml_p2(
            list(
                map(
                    add, build_robot_no_check("geode", resources, robots, bp)[0], robots
                )
            ),
            build_robot_no_check("geode", resources, robots, bp)[1],
            time + 1,
            bp,
        )
        # print("GEODE ROBOT BUILD")
        return
    if resources[0] >= bp[2][0] and resources[1] >= bp[2][1] and robots[2] < bp[3][1]:
        fml_p2(
            list(
                map(add, build_robot_no_check("obs", resources, robots, bp)[0], robots)
            ),
            build_robot_no_check("obs", resources, robots, bp)[1],
            time + 1,
            bp,
        )
    if resources[0] >= bp[1] and robots[1] < bp[2][1]:
        fml_p2(
            list(
                map(add, build_robot_no_check("clay", resources, robots, bp)[0], robots)
            ),
            build_robot_no_check("clay", resources, robots, bp)[1],
            time + 1,
            bp,
        )
        # print("CLAY ROBOT BUILD")

    if resources[0] >= bp[0] and robots[0] < max([bp[0], bp[1], bp[2][0], bp[3][0]]):
        fml_p2(
            list(
                map(add, build_robot_no_check("ore", resources, robots, bp)[0], robots)
            ),
            build_robot_no_check("ore", resources, robots, bp)[1],
            time + 1,
            bp,
        )
    fml_p2(list(map(add, resources, robots)), robots, time + 1, bp)
    state.add(
        (
            tuple(
                (
                    resources[0],
                    resources[1],
                    resources[2],
                    resources[3],
                    robots[0],
                    robots[1],
                    robots[2],
                    robots[3],
                    time,
                )
            )
        )
    )
    return


for y in range(len(ic)):
    y
    d = {}
    for i in range(25):
        d[i] = [0, 0, 0, 0]

    state = set()

    fml([0, 0, 0, 0], [1, 0, 0, 0], 0, ic[y])
    print(d[24][3], d[24][3] * (y + 1))
    solution_1 = d[24][3] * (y + 1) + solution_1


for y in range(3):
    print(y + 1)
    d = {}
    for i in range(33):
        d[i] = [0, 0, 0, 0]

    state = set()

    fml_p2([0, 0, 0, 0], [1, 0, 0, 0], 0, ic[y])
    print(d[32][3])
    solution_2 = d[32][3] * solution_2


# d = {}
# for i in range(33):
#     d[i] = [0,0,0,0]

# state = set()

# fml_p2([0,0,0,0], [1,0,0,0], 0, ic[0])
# print(d[32][3])


print("Part One : " + str(solution_1) + "\nPart Two : " + str(solution_2))
