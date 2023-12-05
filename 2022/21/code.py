# Advent of code Year 2022 Day 21 solution
# Author = brauni
# Date = 2022-12-27
"https://adventofcode.com/2022/day/21"

import re
from collections import Counter
import copy
import os
import math
from sympy import symbols, solve

solution_1, solution_2=0, 0

# with open(os.getcwd() + "/2022/21/example.txt", 'r') as f:
with open(os.getcwd() + "/2022/21/input.txt", 'r') as f:
    input = f.read()
    input = input.split("\n")
    # input = []
    # for line in f.readlines():
        # input.append(int(line))
    # input = [int(line) for line in f.readlines()]
    # input = [line for line in f.readlines()]

# PART 0

from datetime import datetime
startTime = datetime.now()


ic = {}
for line in input:
	line = line.split(": ")
	ic[line[0]] = "".join([str(x) for x in line[1:]])

ignore = set()
for key in ic:
	if re.search('[a-z]',ic[key]) == None:
		ic[key] = int(ic[key])
		ignore.add(key)

abc = 0
while not isinstance(ic['root'],int):
	abc +=1
	for key in ic:
		if key in ignore:
			continue
		x = ic[key]
		x = x.split()
		x = [' ( ' + str(ic[t]) +  ' ) ' if re.search('[\*\/\-\+\d\s\(\)]+',t) == None else t for t in x]
		if re.search('[a-z]+'," ".join([str(b) for b in x])) == None:
			ic[key] = int(eval(" ".join([str(b) for b in x])))
			ignore.add(key)
		else:
			ic[key] = " ".join([str(b) for b in x])

solution_1 = ic["root"]

# PART 2
ic = {}
for line in input:
	line = line.split(": ")
	ic[line[0]] = "".join([str(x) for x in line[1:]])

ignore = set()
for key in ic:
	if re.search('[a-z]',ic[key]) == None:
		ic[key] = int(ic[key])
		ignore.add(key)
ignore.add('humn')
ic['humn'] = 'humn'
operators = ['/','*','-','+']

ic["root"] = " ".join(["=" if x in operators else x for x in ic["root"].split()])

# while not isinstance(ic['root'],int):
for u in range(abc):
	for key in ic:
		if key in ignore:
			continue
		x = ic[key]
		x = x.split()
		x = [' ( ' + str(ic[t]) +  ' ) ' if re.search('[\*\/\-\+\d\s\(\)\=]+',t) == None else t for t in x]
		if re.search('[a-z]+'," ".join([str(b) for b in x])) == None:
			ic[key] = int(eval(" ".join([str(b) for b in x])))
			ignore.add(key)
		else:
			ic[key] = " ".join([str(b) for b in x])
	# print(ic)


r0, r1 = ic["root"].split('=')
r1 = int(eval(r1))
r0 = " ".join(["x" if x == 'humn' else x for x in r0.split()])

r0 = " ".join([r0,'- ' + str(r1) ])

x = symbols('x')
expr = r0

solution_2 = solve(expr)[0]


# SOLUTIONS
print(datetime.now() - startTime)
print("Part One : "  + str(solution_1) + "\nPart Two : " + str(solution_2))