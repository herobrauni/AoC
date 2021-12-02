# Advent of code Year 2020 Day 9 solution
# Author = brauni
# Date = 2021-12-01

# with open("C:\\Users\\brauni\\Documents\\GitHub\\AoC\\2020\\09\\example.txt", 'r') as f:
with open("C:\\Users\\brauni\\Documents\\GitHub\\AoC\\2020\\09\\input.txt", 'r') as f:
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
test = input.copy()
for i in range(0, 25):
    test[i] = True


def find(x, input):
    for y in range(x - 25, x):
        for z in range(x - 25, x):
            if (input[y] != input[z]):
                if (int(input[y]) + int(input[z]) == int(input[x])):
                    return True


for x in range(25, len(input)):
    boo = False
    boo = find(x, input)
    if (boo):
        test[x] = True

for u in test:
    if(u != True):
        solution_1 = u
        break

print("Part One : " + str(solution_1))


# PART 2
for i in range(len(input)):
    input[i] = int(input[i])

zahl = int(solution_1)

input = [f for f in input if f < zahl]
lists = [[]]

for i in range(len(input) + 1):
    for j in range(i + 1, len(input) + 1):
        sub = input[i:j]
        if(sum(sub) > zahl):
            break
        lists.append(sub)
        # print(sub)

# print(len(lists))

for x in lists:
    bla = sum(x)
    if (bla == zahl):
        solution_2 = (min(x) + max(x))


print("Part Two : " + str(solution_2))
