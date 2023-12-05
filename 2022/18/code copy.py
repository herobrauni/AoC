# Advent of code Year 2022 Day 18 solution
# Author = brauni
# Date = 2022-12-27
"https://adventofcode.com/2022/day/18"

import re
from collections import Counter
import copy
import os
import math
import itertools as it
import numpy as np
import networkx as nx

solution_1, solution_2=0, 0

# with open(os.getcwd() + "/2022/18/example.txt", 'r') as f:
with open(os.getcwd() + "/2022/18/input.txt", 'r') as f:
    input = f.read()
    input = input.split("\n")
    # input = []
    # for line in f.readlines():
        # input.append(int(line))
    # input = [int(line) for line in f.readlines()]
    # input = [line for line in f.readlines()]

# PART 0


print(input)
ic = []
for line in input:
    i = tuple(int(x) for x in line.split(","))
    ic.append(i)

# PART 1
for i in range(len(ic)):
    x = 6
    if (ic[i][0]+1,ic[i][1],ic[i][2]) in ic: x-=1
    if (ic[i][0],ic[i][1]+1,ic[i][2]) in ic: x-=1
    if (ic[i][0],ic[i][1],ic[i][2]+1) in ic: x-=1
    if (ic[i][0]-1,ic[i][1],ic[i][2]) in ic: x-=1
    if (ic[i][0],ic[i][1]-1,ic[i][2]) in ic: x-=1
    if (ic[i][0],ic[i][1],ic[i][2]-1) in ic: x-=1
    # for j in range(len(ic[i])):
    #     if ic[i][j]+1 in [x[j] for x in ic]: x -= 1
    #     if ic[i][j]-1 in [x[j] for x in ic]: x -= 1
    solution_1 += x

# PART 2
xm,ym,zm = range(1,max([int(x[0]) for x in ic])),range(1,max([int(x[1]) for x in ic])),range(1,max([int(x[2]) for x in ic]))
a = [xm,ym,zm]
t = list(it.product(*a))

tp = [tuple(x) for x in t if tuple(x) not in ic]

bla = []

ic_np = [np.array(x) for x in ic]

left = np.array([-1,0,0])
right = np.array([1,0,0])
down = np.array([0,-1,0])
up = np.array([0,1,0])
back = np.array([0,0,1])
forward = np.array([0,0,-1])


G = nx.Graph()

for line in ic:
    G.add_node(line)

for line in tp:
    G.add_node(line)

for i in range(len(ic)):
    if (ic[i][0]+1,ic[i][1],ic[i][2]) in ic: G.add_edge(ic[i], (ic[i][0]+1,ic[i][1],ic[i][2]))
    if (ic[i][0],ic[i][1]+1,ic[i][2]) in ic: G.add_edge(ic[i], (ic[i][0],ic[i][1]+1,ic[i][2]))
    if (ic[i][0],ic[i][1],ic[i][2]+1) in ic: G.add_edge(ic[i], (ic[i][0],ic[i][1],ic[i][2]+1))
    if (ic[i][0]-1,ic[i][1],ic[i][2]) in ic: G.add_edge(ic[i], (ic[i][0]-1,ic[i][1],ic[i][2]))
    if (ic[i][0],ic[i][1]-1,ic[i][2]) in ic: G.add_edge(ic[i], (ic[i][0],ic[i][1]-1,ic[i][2]))
    if (ic[i][0],ic[i][1],ic[i][2]-1) in ic: G.add_edge(ic[i], (ic[i][0],ic[i][1],ic[i][2]-1))

for i in range(len(tp)):
    if (tp[i][0]+1,tp[i][1],tp[i][2]) in tp: G.add_edge(tp[i], (tp[i][0]+1,tp[i][1],tp[i][2]))
    if (tp[i][0],tp[i][1]+1,tp[i][2]) in tp: G.add_edge(tp[i], (tp[i][0],tp[i][1]+1,tp[i][2]))
    if (tp[i][0],tp[i][1],tp[i][2]+1) in tp: G.add_edge(tp[i], (tp[i][0],tp[i][1],tp[i][2]+1))
    if (tp[i][0]-1,tp[i][1],tp[i][2]) in tp: G.add_edge(tp[i], (tp[i][0]-1,tp[i][1],tp[i][2]))
    if (tp[i][0],tp[i][1]-1,tp[i][2]) in tp: G.add_edge(tp[i], (tp[i][0],tp[i][1]-1,tp[i][2]))
    if (tp[i][0],tp[i][1],tp[i][2]-1) in tp: G.add_edge(tp[i], (tp[i][0],tp[i][1],tp[i][2]-1))

outer = []

xx,yy,zz = range(0,max([int(x[0]) for x in ic])+1),range(0,max([int(x[1]) for x in ic])+1),range(0,max([int(x[2]) for x in ic])+1)
a = [xx,yy,zz]
tt = list(it.product(*a))

outer = [tuple(x) for x in tt if x not in ic + tp]

for line in outer:
    G.add_node(line)

for i in range(len(outer)):
    if (outer[i][0]+1,outer[i][1],outer[i][2]) in outer: G.add_edge(outer[i], (outer[i][0]+1,outer[i][1],outer[i][2]))
    if (outer[i][0],outer[i][1]+1,outer[i][2]) in outer: G.add_edge(outer[i], (outer[i][0],outer[i][1]+1,outer[i][2]))
    if (outer[i][0],outer[i][1],outer[i][2]+1) in outer: G.add_edge(outer[i], (outer[i][0],outer[i][1],outer[i][2]+1))
    if (outer[i][0]-1,outer[i][1],outer[i][2]) in outer: G.add_edge(outer[i], (outer[i][0]-1,outer[i][1],outer[i][2]))
    if (outer[i][0],outer[i][1]-1,outer[i][2]) in outer: G.add_edge(outer[i], (outer[i][0],outer[i][1]-1,outer[i][2]))
    if (outer[i][0],outer[i][1],outer[i][2]-1) in outer: G.add_edge(outer[i], (outer[i][0],outer[i][1],outer[i][2]-1))
    ###
    if (outer[i][0]+1,outer[i][1],outer[i][2]) in ic: G.add_edge(outer[i], (outer[i][0]+1,outer[i][1],outer[i][2]))
    if (outer[i][0],outer[i][1]+1,outer[i][2]) in ic: G.add_edge(outer[i], (outer[i][0],outer[i][1]+1,outer[i][2]))
    if (outer[i][0],outer[i][1],outer[i][2]+1) in ic: G.add_edge(outer[i], (outer[i][0],outer[i][1],outer[i][2]+1))
    if (outer[i][0]-1,outer[i][1],outer[i][2]) in ic: G.add_edge(outer[i], (outer[i][0]-1,outer[i][1],outer[i][2]))
    if (outer[i][0],outer[i][1]-1,outer[i][2]) in ic: G.add_edge(outer[i], (outer[i][0],outer[i][1]-1,outer[i][2]))
    if (outer[i][0],outer[i][1],outer[i][2]-1) in ic: G.add_edge(outer[i], (outer[i][0],outer[i][1],outer[i][2]-1))
    ###
    if (outer[i][0]+1,outer[i][1],outer[i][2]) in tp: G.add_edge(outer[i], (outer[i][0]+1,outer[i][1],outer[i][2]))
    if (outer[i][0],outer[i][1]+1,outer[i][2]) in tp: G.add_edge(outer[i], (outer[i][0],outer[i][1]+1,outer[i][2]))
    if (outer[i][0],outer[i][1],outer[i][2]+1) in tp: G.add_edge(outer[i], (outer[i][0],outer[i][1],outer[i][2]+1))
    if (outer[i][0]-1,outer[i][1],outer[i][2]) in tp: G.add_edge(outer[i], (outer[i][0]-1,outer[i][1],outer[i][2]))
    if (outer[i][0],outer[i][1]-1,outer[i][2]) in tp: G.add_edge(outer[i], (outer[i][0],outer[i][1]-1,outer[i][2]))
    if (outer[i][0],outer[i][1],outer[i][2]-1) in tp: G.add_edge(outer[i], (outer[i][0],outer[i][1],outer[i][2]-1))


lul = []

for line in tp:
    if nx.has_path(G, line, outer[0]):
        continue
    else:
        lul.append(line)

len(lul)
len(ic)

for i in range(len(lul)):
    x = 6
    if (lul[i][0]+1,lul[i][1],lul[i][2]) in lul: x-=1
    if (lul[i][0],lul[i][1]+1,lul[i][2]) in lul: x-=1
    if (lul[i][0],lul[i][1],lul[i][2]+1) in lul: x-=1
    if (lul[i][0]-1,lul[i][1],lul[i][2]) in lul: x-=1
    if (lul[i][0],lul[i][1]-1,lul[i][2]) in lul: x-=1
    if (lul[i][0],lul[i][1],lul[i][2]-1) in lul: x-=1
    solution_2 += x

solution_1 - solution_2