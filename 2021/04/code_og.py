# Advent of code Year 2021 Day 4 solution
# Author = brauni
# Date = 2021-12-04
# Working, but slow and bad code.


import re
from collections import Counter
import copy

solution_1, solution_2 = "", ""

# with open("C:\\Users\\brauni\\Documents\\GitHub\\AoC\\2021\\04\\example.txt", 'r') as f:
with open("C:\\Users\\brauni\\Documents\\GitHub\\AoC\\2021\\04\\input.txt", 'r') as f:
    # input = f.read()
    # input = input.split("\n")
    # input = []
    # for line in f.readlines():
    # input.append(int(line))
    # input = [int(line) for line in f.readlines()]
    # input = [line for line in f.readlines()]
    file = f.read()
    draws = [file.split("\n\n")[0]]
    draws = [int(line) for line in draws[0].split(",")]
    input = file.split("\n\n")[1:]
    input = [line.split("\n") for line in input]

"""
print(input)
print(draws)
"""
fields_og = []
for i in range(len(input)):
    for j in range(len(input[i])):
        x = [y for y in input[i][j].split(" ") if y != " "]
        x = [int(y) for y in x if y != ""]
        fields_og.append(x)


# PART 1
fields = copy.deepcopy(fields_og)
for draw in draws:
    for i in range(len(fields)):
        for j in range(len(fields[i])):
            if fields[i][j] == draw:
                fields[i][j] = -1

    # check if bingo
    for x in range(0, len(fields), 5):
        for y in range(0, 5):
            if sum(fields[x+y]) == -5:
                print("horizontal: ", x, draw)
                break
            if sum([row[0+y] for row in fields[x:x + 5]]) == -5:
                print("vertical: ", x, draw)
                break
        else:
            continue
        break
    else:
        continue
    break

t = 0
for i in range(0, 5):
    t += sum([row for row in fields[i+x]if row != -1])

solution_1 = t * draw
# PART 2

fields_p2 = copy.deepcopy(fields_og)
temp_remove = []
for draw in draws:
    for i in range(len(fields_p2)):
        for j in range(len(fields_p2[i])):
            if fields_p2[i][j] == draw:
                fields_p2[i][j] = -1
    # check if bingo
        for x in range(0, len(fields_p2), 5):
            for y in range(0, 5):
                if sum(fields_p2[x+y]) == -5:
                    for u in range(5):
                        # print(fields_p2[x+u])
                        temp_remove.append(x)  # give indexes
                if sum([row[0+y] for row in fields_p2[x:x + 5]]) == -5:
                    for u in range(5):
                        # print(fields_p2[x+u])
                        temp_remove.append(x)  # give indexes
            temp_remove = list(dict.fromkeys(temp_remove))
            if len(temp_remove) == (len(fields_p2) // 5 - 1):
                break
        else:
            continue
        break
    else:
        continue
    break
# else:
#     continue
# break

temp = []
for i in range(0, len(fields_og), 5):
    if i not in temp_remove:
        for j in range(0, 5):
            temp.append(fields[i+j])

for draw in draws:
    for i in range(len(temp)):
        for j in range(len(temp[i])):
            if temp[i][j] == draw:
                temp[i][j] = -1

    # check if bingo
    for x in range(0, len(temp), 5):
        for y in range(0, 5):
            if sum(temp[x+y]) == -5:
                print("horizontal: ", x, draw)
                break
            if sum([row[0+y] for row in temp[x:x + 5]]) == -5:
                print("vertical: ", x, draw)
                break
        else:
            continue
        break
    else:
        continue
    break


t = 0
for i in range(0, 5):
    t += sum([row for row in temp[i+x]if row != -1])

solution_2 = t * draw

# SOLUTIONS

print("Part One : " + str(solution_1) + "\nPart Two : " + str(solution_2))
