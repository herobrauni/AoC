# Advent of code Year 2022 Day 20 solution
# Author = brauni
# Date = 2022-12-27
"https://adventofcode.com/2022/day/20"

import re
from collections import Counter, deque
import copy
import os
import math

solution_1, solution_2=0, 0

# with open(os.getcwd() + "/2022/20/example.txt", 'r') as f:
with open(os.getcwd() + "/2022/20/input.txt", 'r') as f:
    input = f.read()
    input = [int(x)*811589153 for x in input.split("\n")]
    # input = []
    # for line in f.readlines():
        # input.append(int(line))
    # input = [int(line) for line in f.readlines()]
    # input = [line for line in f.readlines()]

# PART 0

instructions = copy.deepcopy(input)
crypt = [x for x in range(len(instructions))]

def find_index(l, target):
	for i in range(len(l)):
		if l[i] == target:
			return i

print([instructions[x] for x in crypt])
for z in range(10):
	for i in range(len(instructions)):
		if instructions[i] == 0:
			continue
		cursor = find_index(crypt, i)
		tmp = crypt.pop(cursor)
		if (cursor+instructions[i]) == 0:
			crypt.append(tmp)
		else:
			# inspos = (cursor+instructions[i])%len(crypt) if instructions[i] > 0 else -((cursor+instructions[i])%len(crypt))
			inspos = (cursor+instructions[i])%len(crypt)
			crypt.insert(inspos,tmp)
		# if [instructions[x] for x in crypt] != example[i+1]:
		# 	print(f'failed for operation {instructions[i]} with cursor {cursor}: {[instructions[x] for x in crypt]} should be {example[i+1]}')
		# 	break
		# print([instructions[x] for x in crypt])

# # PART 1
bla = [instructions[x] for x in crypt]

solution_2 = bla[(find_index(bla, 0)+1000)%len(bla)] + bla[(find_index(bla, 0)+2000)%len(bla)] + bla[(find_index(bla, 0)+3000)%len(bla)]

# PART 2



# SOLUTIONS

print("Part One : "  + str(solution_1) + "\nPart Two : " + str(solution_2))