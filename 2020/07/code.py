# Advent of code Year 2020 Day 7 solution
# Author = brauni
# Date = 2021-12-01
import re

# with open("C:\\Users\\brauni\\Documents\\GitHub\\AoC\\2020\\07\\example.txt", 'r') as f:
with open("C:\\Users\\brauni\\Documents\\GitHub\\AoC\\2020\\07\\input.txt", 'r') as f:
    # input = f.read()
    # input = input.split("\n")
    # input = []
    # for line in f.readlines():
    # input.append(int(line))
    #input = [int(line) for line in f.readlines()]
    input = [line for line in f.readlines()]

"""
print(input)
"""


# PART 1
dic = {}
temp_input = input.copy()
for i in range(len(temp_input)):
    temp_input[i] = temp_input[i].strip()
    temp_input[i] = temp_input[i].replace("bags", "")
    temp_input[i] = temp_input[i].replace("bag", "")
    temp_input[i] = re.split(" contain |, ", temp_input[i])

    for j in range(len(temp_input[i])):
        temp_input[i][j] = temp_input[i][j].strip(".")
        temp_input[i][j] = temp_input[i][j].strip()
        temp_input[i][j] = re.sub(r"\d ", "", temp_input[i][j])
    # print(input[i])
for l in temp_input:
    for m in range(len(l)):
        if (m > 0 and "no other" not in l[m]):
            if (l[m] not in dic):
                dic[str(l[m])] = []
            dic[str(l[m])].append(l[0])

lists = []


def find_1(color, lists):
    if color in dic:
        for x in dic[color]:
            lists.append(x)
            find_1(x, lists)
    return lists


lists = find_1("shiny gold", lists)
lists = set(lists)

print("Part One : " + str(len(lists)))


# PART 2
dic = {}
for i in range(len(input)):
    input[i] = input[i].strip()
    input[i] = input[i].replace("bags", "")
    input[i] = input[i].replace("bag", "")
    input[i] = re.split(" contain |, ", input[i])

    for j in range(len(input[i])):
        input[i][j] = input[i][j].strip(".")
        input[i][j] = input[i][j].strip()
        # input[i][j] = re.sub(r"\d ", "", input[i][j])
    # print(input[i])
for l in input:
    for m in range(len(l)):
        if (m > 0 and "no other" not in l[m]):
            if (l[0] not in dic):
                dic[str(l[0])] = []
            dic[str(l[0])].append(l[m])

# print(dic)

lists = []


def find_2(color):
    # print(color)
    count = 0
    if color in dic:
        for x in dic[color]:
            z = int(x[0])
            pew = re.split(r"\d ", x)
            bla = find_2(pew[1])
            if (bla is None):
                bla = z
                # print(z)
            else:
                bla = z * bla
            count = count + bla
            # print(count, bla, z)
    else:
        return None
    # print(color, count)
    return count + 1


print("Part Two : " + str((find_2("shiny gold") - 1)))
