# Advent of code Year 2021 Day 1 solution
# Author = brauni
# Date = 2021-12-01

# Part 1
with open("C:\\Users\\brauni\\Documents\\GitHub\\AoC\\2021\\01\\input.txt", 'r') as f:
    input = []
    for line in f.readlines():
        input.append(int(line))

c = 0
for i in range(1, len(input)):
    if input[i] > input[i-1]:
        c += 1

print("Part One : " + str(c))


# Part 2
d = 0
for i in range(len(input)):
    sum_first = sum(input[i:i+3])
    sum_second = sum(input[i+1:i+4])
    if sum_first < sum_second:
        d += 1

print("Part Two : " + str(d))
