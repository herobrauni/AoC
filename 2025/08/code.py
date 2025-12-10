# Advent of Code Year 2025 Day 8 solution
# Author = brauni
# Date = 2025-12-08

import re
import os
import math
from aocd import submit
from aocd.models import Puzzle
puzzle = Puzzle(year=2025, day=8)


# with open(os.getcwd() + "/2025/08/example.txt", 'r') as f:
with open(os.getcwd() + "/AoC_private/2025/08/input.txt", 'r') as f:
    # input = f.read()
    # input = input.split("\n")
    input = []
    for line in f.readlines():
        line = line.split(",")
        input.append((int(line[0]),int(line[1]),int(line[2].strip())))
    # input = [int(line) for line in f.readlines()]
    # input = [line for line in f.readlines()]

print(input)

# PART 1
solution_1 = 0

cycles = 1000

bla = {}
# calculate all distances?
for i, key1 in enumerate(input):
    for key2 in input[i+1:]:
        distance = math.dist(key1, key2)
        bla[distance] = (key1, key2)

sorted_bla = sorted(bla.items(), key=lambda item: item[0])

pairs = []
for i in range(len(bla)):
    point_a = sorted_bla[i][1][0]
    point_b = sorted_bla[i][1][1]
    pairs.append((point_a,point_b))

connections = []

for pair in pairs[:cycles]:
    matching_connections = [con for con in connections if pair[0] in con or pair[1] in con]
    
    if not matching_connections:
        # new connection if pair does not exist
        connections.append(set([pair[0], pair[1]]))
    else:
        # add all to the first connection
        merged = matching_connections[0]
        merged.update([pair[0], pair[1]])
        
        # delete others
        for con in matching_connections[1:]:
            merged.update(con)
            connections.remove(con)


connection_lenghts = sorted([len(x) for x in connections], reverse=True)
solution_1 = math.prod(connection_lenghts[:3])

### SOLUTION 1
print("Part One : " + str(solution_1))

submit(solution_1, part="a", day=8, year=2025)



# PART 2
solution_2 = 0

# connections = []
while True:
    for pair in pairs[cycles:]:
        matching_connections = [con for con in connections if pair[0] in con or pair[1] in con]
        if not matching_connections:
            # new connection if pair does not exist
            connections.append(set([pair[0], pair[1]]))
        else:
            # add all to the first connection
            merged = matching_connections[0]
            merged.update([pair[0], pair[1]])
            
            # delete others
            for con in matching_connections[1:]:
                merged.update(con)
                connections.remove(con)
        if len(connections) == 1 and len(connections[0]) == len(input):
            finished = True
            break
    if finished:
        break

solution_2 = pair[0][0] * pair[1][0]

### SOLUTION 2
print("Part Two : " + str(solution_2))

submit(solution_2, part="b", day=8, year=2025)
