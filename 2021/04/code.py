# Advent of code Year 2021 Day 4 solution
# Author = brauni
# Date = 2021-12-04
from os import remove
import re
from collections import Counter
import copy

solution_1, solution_2 = "", ""
# with open("C:\\Users\\brauni\\Documents\\GitHub\\AoC\\2021\\04\\example.txt", 'r') as f:
with open("C:\\Users\\brauni\\Documents\\GitHub\\AoC\\2021\\04\\input.txt", "r") as f:
    # input = f.read()
    # input = input.split("\n")
    # input = []
    # for line in f.readlines():
    # input.append(int(line))
    # input = [int(line) for line in f.readlines()]
    file = f.read()

# Split the file and use the first line for draws (Bingo Numbers)
draws = [int(line) for line in file.split("\n\n")[0].split(",")]
# Split the file and use all except first line for Input
input = [line.split("\n") for line in file.split("\n\n")[1:]]

# convert all strings to ints while removing whitespaces
# End up with fields[][] containing Bingo Sheets
fields_orginal = []
for i in range(len(input)):
    for j in range(len(input[i])):
        row = [line for line in input[i][j].split(" ") if line != " "]
        row = [int(line) for line in row if line != ""]
        fields_orginal.append(row)

"""
print(input)
"""

# PART 1
# Deepcopy to actually make a copy of the WHOLE list, fuck you shallow copy
fields = copy.deepcopy(fields_orginal)


def mark_bingo_numbers_on_sheets(fields, draw):
    # Loop through each Number of the Bingo Fields and convert current Draw Number to -1 to find them later
    for i in range(len(fields)):
        for j in range(len(fields[i])):
            if fields[i][j] == draw:
                fields[i][j] = -1


def check_for_bingo(fields):
    # Check if any row or column has all elements as -1 -> sum of -5
    # if so, return the startrow of the winning bingo field
    all_bingo_rows_for_this_round = []
    for x in range(0, len(fields), 5):
        for y in range(0, 5):
            if (sum(fields[x + y]) == -5 or sum([row[0 + y] for row in fields[x: x + 5]]) == -5):
                all_bingo_rows_for_this_round.append(x)
    # Remove duplicates from the list
    all_bingo_rows_for_this_round = list(
        dict.fromkeys(all_bingo_rows_for_this_round))
    return all_bingo_rows_for_this_round


# Loop through all draws, mark the Bingo Numbers on the sheets and check for Bingo
# if Bingo is found, sum up the remaining numbers on the winning field and multiply by last draw for solution 1
for draw in draws:
    mark_bingo_numbers_on_sheets(fields, draw)
    bingo_rows = check_for_bingo(fields)
    if len(bingo_rows) == 1:
        solution_1 = draw * sum([sum([ele for ele in sub if ele != -1])
                                for sub in fields[bingo_rows[0]: bingo_rows[0] + 5]])
        break

# PART 2
fields = copy.deepcopy(fields_orginal)

solution = []
# run until only one board is left over
for draw in draws:
    if len(check_for_bingo(fields)) == (len(fields) // 5 - 1):
        # get index of remaining board
        start_of_remaining_board = [i for i in range(
            0, len(fields), 5) if i not in check_for_bingo(fields)]

        # create new list "solution" with the remaining board
        solution = fields[start_of_remaining_board[0]
            :start_of_remaining_board[0] + 5]
        break
    mark_bingo_numbers_on_sheets(fields, draw)


# Find the bingo on the last board
# sum all remaining numbers and multiply by last draw for solution 2
for draw in draws:
    mark_bingo_numbers_on_sheets(solution, draw)
    if len(check_for_bingo(solution)) == 1:
        solution_2 = draw * \
            sum([sum([ele for ele in sub if ele != -1]) for sub in solution])
        break


# SOLUTIONS

print("Part One : " + str(solution_1) + "\nPart Two : " + str(solution_2))
