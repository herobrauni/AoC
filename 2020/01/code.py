# Advent of code Year 2020 Day 1 solution
# Author = brauni
# Date = 2021-12-01

# with open("C:\\Users\\brauni\\Documents\\GitHub\\AoC\\2020\\01\\example.txt", 'r') as f:
with open("C:\\Users\\brauni\\Documents\\GitHub\\AoC\\2020\\01\\input.txt", 'r') as f:
    # input = f.read()
    # input = input.split("\n")
    # input = []
    # for line in f.readlines():
    # input.append(int(line))
    input = [int(line) for line in f.readlines()]
    #input = [line for line in f.readlines()]

"""
print(input)
"""


# PART 1

input.sort()
l1, l2 = [f for f in input if f <= 2020 /
          2], [f for f in input if f > 2020 / 2]
for z in input:
    if (2020 - z in l2):
        solution_1 = z * (2020 - z)
        break


print("Part One : " + str(solution_1))


# PART 2

l1, l2 = [f for f in input if f <= 2020 /
          2], [f for f in input if f > 2020 / 2]

l1_combined = []
for f in l1:
    for x in l1:
        l1_combined.append(f + x)
l1_combined = list(set(l1_combined))
l1_combined.sort()
for f in l1_combined:
    for x in l1:
        if (f + x == 2020):
            print(f, x)
            break
    if (2020 - f in l2):
        for y in l1:
            if (f - y in l1):
                print(f - y, y, 2020 - f)
                solution_2 = (f - y) * y * (2020 - f)
                break

print("Part Two : " + str(solution_2))
