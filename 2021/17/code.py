# Advent of code Year 2021 Day 17 solution
# Author = brauni
# Date = 2021-12-17
"https://adventofcode.com/2021/day/17"

import re
from collections import Counter
import copy
import os
import math

solution_1, solution_2 = 0, 0

# with open(os.getcwd() + "\\2021\\17\\example.txt", 'r') as f:
with open(os.getcwd() + "\\2021\\17\\input.txt", "r") as f:
    input = f.read()


# PART 0
target_area_x = int(input.split(" ")[2].split("=")[1].split("..")[0]), int(
    input.split(" ")[2].split("=")[1].split("..")[1].strip(",")
)
target_area_y = int(input.split(" ")[3].split("=")[1].split("..")[0]), int(
    input.split(" ")[3].split("=")[1].split("..")[1]
)


# PART 1
# Does simulate the shot trajectory
# if the shell ends up below the target area we end, because it will only go lower from here
# we check if any of the path plot points were in the target area
# if so it was a hit, else we missed
def shoot(trajectory, target_area_x, target_area_y):
    path = []
    projectile_position = (0, 0)
    y = -99999999
    while not projectile_position[1] < min(target_area_y):
        projectile_position = (
            projectile_position[0] + trajectory[0],
            projectile_position[1] + trajectory[1],
        )
        # print(projectile_position, trajectory)
        trajectory[0] += 1 if trajectory[0] < 0 else 0
        trajectory[0] -= 1 if trajectory[0] > 0 else 0
        trajectory[1] -= 1
        if projectile_position[1] > y:
            y = projectile_position[1]
        path.append(projectile_position)
    for x in path:
        if x[0] in range(target_area_x[0], target_area_x[1] + 1) and x[1] in range(
            target_area_y[0], target_area_y[1] + 1
        ):
            return "HIT", y
    else:
        return "MISS", y


highest_y = -99999999
hits = 0

# we simulate the trajectory for each angle and check for hits and the highest y points reached
# x velocity cant go higher than the right side of the target area, otherwise we would shoot through in step 1
for x in range(0, max(target_area_x) + 1):
    # y velocity should be between the lowest point and the lowest point * -1 (dont know why, but works like this)
    for y in range(min(target_area_y), abs(min(target_area_y))):
        t1 = 0
        trajectory = [x, y]
        result, high_y = shoot(trajectory, target_area_x, target_area_y)
        if result == "HIT":
            hits += 1
            if high_y > highest_y:
                highest_y = high_y

solution_1 = highest_y
# PART 2
solution_2 = hits

# SOLUTIONS

print("Part One : " + str(solution_1) + "\nPart Two : " + str(solution_2))
assert solution_1 == 2775
assert solution_2 == 1566
