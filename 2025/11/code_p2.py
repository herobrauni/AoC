# Advent of Code Year 2025 Day 11 solution
# Author = brauni
# Date = 2025-12-11

import os
from functools import cache

import networkx as nx
from aocd import submit
from aocd.models import Puzzle

puzzle = Puzzle(year=2025, day=11)


# with open(os.getcwd() + "/2025/11/example.txt", "r") as f:
with open(os.getcwd() + "/AoC_private/2025/11/input.txt", "r") as f:
    input = f.read()
    input = input.split("\n")
    # input = []
    # for line in f.readlines():
    # input.append(int(line))
    # input = [int(line) for line in f.readlines()]
    # input = [line for line in f.readlines()]

# print(input)


nodes = dict()
for line in input:
    line = line.replace(":", "")
    line = line.split(" ")
    nodes[line[0]] = line[1:]

graph = nx.DiGraph()

for node in nodes:
    for edge in nodes[node]:
        graph.add_edge(node, edge)

# PART 2
solution_2 = 0


@cache
def count_paths(a, b):
    if a == b:
        return 1
    total = 0
    for next in graph.successors(a):
        total += count_paths(next, b)
    return total


# dac -> fft
p1 = count_paths("svr", "dac")
p2 = count_paths("dac", "fft")
p3 = count_paths("fft", "out")
solution_2 += p1 * p2 * p3

# fft -> dac
p4 = count_paths("svr", "fft")
p5 = count_paths("fft", "dac")
p6 = count_paths("dac", "out")
solution_2 += p4 * p5 * p6


print("Part Two : " + str(solution_2))

submit(solution_2, part="b", day=11, year=2025)
