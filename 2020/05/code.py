# Advent of code Year 2020 Day 5 solution
# Author = brauni
# Date = 2021-12-01

# with open(os.getcwd() + "\\2020\\05\\example.txt", 'r') as f:
with open(os.getcwd() + "\\2020\\05\\input.txt", 'r') as f:
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
uid = 0
uidlist = []
for x in input:
    rows = [0, 127]
    columns = [0, 7]
    x = x.strip()
    for i in range(0, len(x) - 3):
        if (x[i] == "F"):
            rows[1] = rows[1] - pow(2, 6-i)
        elif (x[i] == "B"):
            rows[0] = rows[0] + pow(2, 6 - i)
    for i in range(len(x) - 3, len(x)):
        if (x[i] == "L"):
            columns[1] = columns[1] - pow(2, 9 - i)
        elif (x[i] == "R"):
            columns[0] = columns[0] + pow(2, 9 - i)
    if (rows[0] == rows[1] and columns[0] == columns[1]):
        uidlist.append(rows[0] * 8 + columns[0])
        if (uid < (rows[0] * 8 + columns[0])):
            uid = rows[0] * 8 + columns[0]
uidlist.sort()

print("Part One : " + str(uidlist[-1]))


# PART 2

for i in range(len(uidlist)-1):
    if (uidlist[i + 1] != uidlist[i] + 1):
        solution_2 = uidlist[i] + 1

print("Part Two : " + str(solution_2))
