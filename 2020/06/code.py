# Advent of code Year 2020 Day 6 solution
# Author = brauni
# Date = 2021-12-01

# with open("C:\\Users\\brauni\\Documents\\GitHub\\AoC\\2020\\06\\example.txt", 'r') as f:
with open("C:\\Users\\brauni\\Documents\\GitHub\\AoC\\2020\\06\\input.txt", 'r') as f:
    # input = f.read()
    # input = input.split("\n")
    # input = []
    # for line in f.readlines():
    # input.append(int(line))
    # input = [int(line) for line in f.readlines()]
    # input = [line for line in f.readlines()]
    input = f.read().split("\n\n")

"""
print(input)
"""


# PART 1
count = 0
for x in input:
    x = x.replace("\n", "")
    x = set(x)
    count = count + len(x)

print("Part One : " + str(count))


# PART 2
z = 0
for x in input:
    o = 0
    count = 1
    for y in x:
        if (y == "\n"):
            count += 1
    x = x.replace("\n", "")
    bla = set(x)
    for i in bla:
        c = x.count(i)
        if (c == count):
            z += 1
            o += 1
    # print(x, "\n", bla, "\n", count, o)

print("Part Two : " + str(z))
