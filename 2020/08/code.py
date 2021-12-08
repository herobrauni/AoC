# Advent of code Year 2020 Day 8 solution
# Author = brauni
# Date = 2021-12-01
import re
import os
# with open(os.getcwd() + "\\2020\\08\\example.txt", 'r') as f:
with open(os.getcwd() + "\\2020\\08\\input.txt", 'r') as f:
    input = f.read()
    input = input.split("\n")
    # input = []
    # for line in f.readlines():
    # input.append(int(line))
    # input = [int(line) for line in f.readlines()]
    # input = [line for line in f.readlines()]

"""
print(input)
"""


# PART 1
i = 0
acc = 0
visited = []
while i < len(input):
    y = input[i].split(" ")
    if (i in visited):
        print("fuck")
        break
    else:
        visited.append(i)
    if (y[0] == "nop"):
        # print(i+1, input[i])
        i += 1
    elif (y[0] == "acc"):
        acc = acc + int(y[1])
        i += 1
    elif (y[0] == "jmp"):
        i = i + int(y[1])
    # print(i+1, input[i], acc)

print("Part One : " + str(acc))


# PART 2
for i in range(len(input)):
    input[i] = input[i].split(" ")


# print(input)
for j in range(len(input)):
    i = 0
    acc = 0
    visited = []
    change = False
    if (input[j][0] == "jmp"):
        input[j][0] = "nop"
        change = True
    # print(j+1, input[j][0])
    while (True):
        if (i + 1 in visited):
            # print("duplicate")
            break
        else:
            visited.append(i + 1)
        if (i >= len(input)):
            solution_2 = acc
            # print(acc)
            # print(i)
            break
        if (input[i][0] == "nop"):
            i += 1
        elif (input[i][0] == "acc"):
            acc = acc + int(input[i][1])
            i += 1
        elif (input[i][0] == "jmp"):
            # print(i, input[i])
            i = i + int(input[i][1])
    # print(acc, visited)
    if (input[j][0] == "nop" and change == True):
        input[j][0] = "jmp"
# print(input)


print("Part Two : " + str(solution_2))
