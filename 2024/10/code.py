# Advent of Code Year 2024 Day 10 solution
# Author = brauni
# Date = 2024-12-10

import itertools
import networkx
import os
from aocd import submit
from aocd.models import Puzzle
puzzle = Puzzle(year=2024, day=10)

# with open(os.getcwd() + "/2024/10/example.txt", 'r') as f:
with open(os.getcwd() + "/AoC_private/2024/10/input.txt", 'r') as f:
    input = f.read()
    input = input.split("\n")


# print(input)


f = {}
trailheads = []
ends = []

for n, line in enumerate(input):
    for m, x in [(m, int(y)) for m, y in enumerate(line)]:
        f[complex(m, n)] = x
        if x == 0:
            trailheads.append(complex(m, n))
        elif x == 9:
            ends.append(complex(m, n))


def create_graph(f):
    g = networkx.DiGraph()
    g.add_nodes_from(f.keys())
    directions = [complex(0, -1), complex(1, 0), complex(0, 1), complex(-1, 0)]
    for pos in f.keys():
        for dir in directions:
            if pos+dir in f.keys():
                if f[pos]+1 == f[pos+dir]:
                    g.add_edge(pos, pos+dir)
    return g


g = create_graph(f)

# PART 1
solution_1 = 0

p2_to_check = []
for x in itertools.product(trailheads, ends):
    if networkx.has_path(g, x[0], x[1]):
        p2_to_check.append(x)

solution_1 = len(p2_to_check)
# SOLUTION 1
print("Part One : " + str(solution_1))

submit(solution_1, part="a", day=10, year=2024)


# PART 2
solution_2 = 0

for x in p2_to_check:
    solution_2 += len(list(networkx.all_simple_paths(g, x[0], x[1])))

# SOLUTION 2
print("Part Two : " + str(solution_2))

submit(solution_2, part="b", day=10, year=2024)
