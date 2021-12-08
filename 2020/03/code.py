# Advent of code Year 2020 Day 3 solution
# Author = brauni
# Date = 2021-12-01

# with open(os.getcwd() + "\\2020\\03\\example.txt", 'r') as f:
with open(os.getcwd() + "\\2020\\03\\input.txt", 'r') as f:
    # input = f.read()
    # input = input.split("\n")
    # input = []
    # for line in f.readlines():
    # input.append(int(line))
    #input = [int(line) for line in f.readlines()]
    input = [line.strip() for line in f.readlines()]

"""
print(input)
"""


# PART 1
i = 0
solution_1 = 0
for l in input:
    if i >= len(l):
        i -= len(l)
    if (l[i] == "#"):
        solution_1 += 1
    i += 3

print("Part One : " + str(solution_1))


# PART 2

lst = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
l = len(input)

total = 1
for steps in lst:
    i = 0
    n = 0
    c = 0
    while n < l:
        if i >= len(input[n]):
            i -= len(input[n])
        if (input[n][i] == '#'):
            c += 1
        i += steps[0]
        n += steps[1]
    total *= c
solution_2 = total
print("Part Two : " + str(solution_2))
