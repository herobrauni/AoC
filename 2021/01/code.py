# Advent of code Year 2021 Day 1 solution
# Author = brauni
# Date = 2021-12-01

# with open(os.getcwd() + "\\2021\\01\\example.txt", 'r') as f:
with open(os.getcwd() + "\\2021\\01\\input.txt", "r") as f:
    # input = f.read()
    # input = input.split("\n")
    # input = []
    # for line in f.readlines():
    #     input.append(int(line))
    input = [int(line) for line in f.readlines()]

"""
print(input)
"""


# PART 1
c = 0
# loop through input list and check if current number is bigger than last number
for i in range(1, len(input)):
    if input[i] > input[i - 1]:
        c += 1
solution_1 = c
print("Part One : " + str(solution_1))


# PART 2
d = 0
# loop through input list and check if the sum of current number + next 2 numbers is smaller than the sum of the next 3 numbers
# sum(1,2,3) < sum(2,3,4)
for i in range(len(input)):
    sum_first = sum(input[i : i + 3])
    sum_second = sum(input[i + 1 : i + 4])
    if sum_first < sum_second:
        d += 1
solution_2 = d
print("Part Two : " + str(solution_2))


# One liners from https://www.reddit.com/r/adventofcode/comments/r66vow/2021_day_1_solutions/hmrggq3/

# create a zip in which the first element of input is matched with the second element of input and so on
# we then iterate through the zip and check if the first element is bigger than the second element
sum(x < y for x, y in zip(input, input[1:]))

# create a zip in which the first element of input is matched with the third element of input and so on
# we then iterate through the zip and check if the first element is bigger than the second element
# this works because for triplets a,b,c and b,c,d, the sum of a,b,c is smaller than the sum of b,c,d if a < b
# because a and d are the only different numbers
sum(x < y for x, y in zip(input, input[3:]))
