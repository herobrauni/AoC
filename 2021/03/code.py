# Advent of code Year 2021 Day 3 solution
# Author = brauni
# Date = 2021-12-03

# could propably be done a little better with Counter from Collections
# so i.e. common = Counter([row[i] for row in input])

# from collections import Counter
import re


# with open("C:\\Users\\brauni\\Documents\\GitHub\\AoC\\2021\\03\\example.txt", 'r') as f:
with open("C:\\Users\\brauni\\Documents\\GitHub\\AoC\\2021\\03\\input.txt", 'r') as f:
    input = f.read()
    input = input.split("\n")
    # input = []
    # for line in f.readlines():
    #     input.append(int(line)))
    # input = [int(line, base=2) for line in f.readlines()]
    # input = [line.strip() for line in f.readlines()]


"""
print(input)
"""


# PART 1
# Could be done by only calculating gamma|epsilon and bit substracions
# gamma ^-1 should be epsilon
gamma, epsilon = "", ""

# loop through all columns of the input
for i in range(len(input[0])):
    # if the sum of all elements (0|1) in the column is bigger than half the number of rows -> common number is 1
    if ((sum([int(row[i]) for row in input])) > len(input) / 2):
        gamma += "1"
        epsilon += "0"
    # if the sum of all elements (0|1) in the column is smaller than half the number of rows -> common number is 0
    else:
        gamma += "0"
        epsilon += "1"
solution_1 = int(gamma, base=2) * int(epsilon, base=2)


# PART 2
# OXYGEN
# use array to store the elements that need removal and remove them at the end of each column run, otherwise it messes with the loop counters
temp_remove = []
temp = input.copy()
# loop through all columns of the input
for i in range(len(temp[0])):
    # stop if only one element is remaining
    if len(temp) == 1:
        break
    # set common to 0 for cases where the sum of all elements (0|1) in the column is equal to half the number of rows
    common = 1
    # if the sum of all elements (0|1) in the column is bigger than half the number of rows set common to 0
    if ((sum([int(row[i]) for row in temp])) > len(temp) / 2):
        common = "1"
    # if the sum of all elements (0|1) in the column is smaller than half the number of rows set common to 1
    elif ((sum([int(row[i]) for row in temp])) < len(temp) / 2):
        common = "0"
    # loop through all remaining rows of the input
    for line in temp:
        # if the i-th element of the row is NOT equal to common we add it to the removal array
        if int(line[i]) != int(common):
            temp_remove.append(line)
    # loop through removal array and remove the elements from the input
    for removal in temp_remove:
        if removal in temp:
            temp.remove(removal)
    # clear the removal array for better performance
    temp_remove = []

# convert the remaining element to an integer
oxygen = int(temp[0], base=2)


# Same as oxygen but with the comparison negated
# use array to store the elements that need removal and remove them at the end of each column run, otherwise it messes with the loop counters
temp_remove = []
temp = input.copy()
# loop through all columns of the input
for i in range(len(temp[0])):
    # stop if only one element is remaining
    if len(temp) == 1:
        break
    # set common to 1 for cases where the sum of all elements (0|1) in the column is equal to half the number of rows
    common = 1
    # if the sum of all elements (0|1) in the column is bigger than half the number of rows set common to 1
    if ((sum([int(row[i]) for row in temp])) > len(temp) / 2):
        common = "1"
    # if the sum of all elements (0|1) in the column is smaller than half the number of rows set common to 0
    elif ((sum([int(row[i]) for row in temp])) < len(temp) / 2):
        common = "0"
    # loop through all remaining rows of the input
    for line in temp:
        # if the i-th element of the row is equal to common we add it to the removal array
        if int(line[i]) == int(common):
            temp_remove.append(line)
    # loop through removal array and remove the elements from the input
    for removal in temp_remove:
        if removal in temp:
            temp.remove(removal)
    # clear the removal array for better performance
    temp_remove = []

# convert the remaining element to an integer
co2 = int(temp[0], base=2)

solution_2 = oxygen * co2

# SOLUTIONS
print("Part One : " + str(solution_1) + "\nPart Two : " + str(solution_2))
