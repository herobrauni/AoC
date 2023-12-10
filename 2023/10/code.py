# Advent of code Year 2023 Day 10 solution
# Author = brauni
# Date = 2023-12-10
"https://adventofcode.com/2023/day/10"

import re
from collections import Counter
import copy
import os
import math
import numpy as np
import networkx as nx
import itertools

solution_1, solution_2=0, 0

with open(os.getcwd() + "/AoC_private/2023/10/input.txt", 'r') as f:
# with open(os.getcwd() + "/2023/10/example.txt", 'r') as f:
    input = f.read()
    input = input.split("\n")
    # input = []
    # for line in f.readlines():
        # input.append(int(line))
    # input = [int(line) for line in f.readlines()]
    # input = [line for line in f.readlines()]

# PART 0


print(input)
grid = np.array([t for t in "".join([x for x in input])])
len(input[0])
len(input)
grid = grid.reshape(len(input),len(input[0]))


# PART 1
s = np.where(grid == "S")
start = (s[0][0],s[1][0])

grid[start]


current = "X"
for direction in [(0,1),(1,0),(0,-1),(-1,0)]:
    if grid[start[0]+direction[0],start[1]+direction[1]] in ["J","-","7"] and direction == (0,1):
        p = (start[0]+direction[0],start[1]+direction[1])
        break
    elif grid[start[0]+direction[0],start[1]+direction[1]] in ["|","J","L"] and direction == (1,0):
        p = (start[0]+direction[0],start[1]+direction[1])
        break
    elif grid[start[0]+direction[0],start[1]+direction[1]] in ["-","F","L"] and direction == (0,-1):
        p = (start[0]+direction[0],start[1]+direction[1])
        break
    elif grid[start[0]+direction[0],start[1]+direction[1]] in ["|","F","7"] and direction == (-1,0):
        p = (start[0]+direction[0],start[1]+direction[1])
        break

length = 0
path = []
path.append(start)
path.append(p)
while current != "S":
# for i in range(100):
    length +=1
    match grid[p]:
        case "|":
            x = (p[0]  +1   , p[1])
            y = (p[0]  -1    , p[1])
            p = x if x not in path else y
        case "-":
            x = (p[0]   , p[1] +1 )
            y = (p[0]     , p[1] -1 )
            p = x if x not in path else y
        case "L":
            x = (p[0] -1  , p[1] )
            y = (p[0]    , p[1] +1)
            p = x if x not in path else y
        case "J":
            x = (p[0] -1      , p[1])
            y = (p[0]      , p[1] -1)
            p = x if x not in path else y
        case "7":
            x = (p[0] +1   , p[1] )
            y = (p[0]     , p[1] -1)
            p = x if x not in path else y
        case "F":
            x = (p[0] +1, p[1] )
            y = (p[0]     , p[1] +1)
            p = x if x not in path else y
        case _:
            print("Error", p,grid[p])
            break
    if p in path:
        print("Error", p,grid[p])
        break
    path.append(p)
    current = grid[p]


solution_1 = round(length/2)

# PART 2
g2 = copy.deepcopy(grid)
g2 = np.pad(g2, pad_width=1, constant_values=".")
pp2 = nx.DiGraph()

# for x in range(len(g2)):
#     for y in range(len(g2[x])):
#         if (x,y) not in path:
#             g2[(x,y)] = "."

# for x in path:
#     match grid[x]:
#         case "J":
#             g2[x] = "⌟"
#         case "L":
#             g2[x] = "⌞"
#         case "F":
#             g2[x] = "⌜"
#         case "7":
#             g2[x] = "⌝"

# for line in g2:
#     print("".join([str(x) for x in line]))


fields = list(itertools.combinations_with_replacement(range(len(g2)),2))
fields = fields + [(x[1],x[0]) for x in fields]
fields = list(set(fields))

path_p2 = [(x[0]+1,x[1]+1) for x in path]
for field in fields:
    pp2.add_node(field)
for field in fields:
    if field not in path_p2:
        for direction in [(0,1),(1,0),(0,-1),(-1,0)]:
            if (field[0]+direction[0],field[1]+direction[1]) not in path_p2:
                pp2.add_edge(field,(field[0]+direction[0],field[1]+direction[1]))

outside = []
for field in fields:
    if field not in path_p2:
        for s in [(0,0),(0,len(g2)-1),(len(g2)-1,0),(len(g2)-1,len(g2)-1)]:
            if nx.has_path(pp2,s,field):
                outside.append(field)
                break

inside = []
for x in range(len(g2)):
    for y in range(len(g2[x])):
        if (x,y) not in path_p2 and (x,y) not in outside:
            g2[(x,y)] = "X"
            inside.append((x,y))
        elif (x,y) in outside:
            g2[(x,y)] = "O"


for line in g2:
    print("".join([str(x) for x in line]))

g2[9,9]
t = (g2 == "X").sum()
solution_2 = t
# (139,139) in fields
# SOLUTIONS

print("Part One : "  + str(solution_1) + "\nPart Two : " + str(solution_2))