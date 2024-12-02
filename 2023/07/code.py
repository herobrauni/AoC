# Advent of code Year 2023 Day 7 solution
# Author = brauni
# Date = 2023-12-07
"https://adventofcode.com/2023/day/7"

import re
from collections import Counter
import copy
import os
import math

solution_1, solution_2 = 0, 0

# with open(os.getcwd() + "/AoC_private/2023/07/input.txt", "r") as f:
with open(os.getcwd() + "/2023/07/example.txt", "r") as f:
    input = f.read()
    input = input.split("\n")
    # input = []
    # for line in f.readlines():
    # input.append(int(line))
    # input = [int(line) for line in f.readlines()]
    # input = [line for line in f.readlines()]

# PART 0


print(input)
ranking = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
hands = [x.split()[0] for x in input]
scores = [int(x.split()[1]) for x in input]
hands2 = {key: [] for key in ["High", "One", "Two", "Three", "Full", "Four", "Five"]}


def comp(hand1, hand2):
    for n, x1 in enumerate(hand1):
        if x1 == hand2[n]:
            continue
        if ranking.index(x1) > ranking.index(hand2[n]):
            return True
        else:
            return False


# PART 1
for x in hands:
    t = Counter(x)
    t = sorted([t[y] for y in list(t)], reverse=True)
    print(x, t)
    if len(t) == 1:
        hands2["Five"].append(x)
        print(x, "Five")
    elif t[0] == 4:
        hands2["Four"].append(x)
        print(x, "Four")
    elif t[0] == 3 and t[1] == 2:
        hands2["Full"].append(x)
        print(x, "Full House")
    elif t[0] == 3:
        hands2["Three"].append(x)
        print(x, "Three")
    elif t[0] == 2 and t[1] == 2:
        hands2["Two"].append(x)
        print(x, "Two Pairs")
    elif len(t) == 4:
        hands2["One"].append(x)
        print(x, "One Pair")
    elif len(t) == 5:
        hands2["High"].append(x)
        print(x, "High Card")

for z in hands2:
    if len(hands2[z]) > 1:
        for i in range(1, len(hands2[z])):
            key = hands2[z][i]
            j = i - 1
            while j >= 0 and comp(key, hands2[z][j]):
                hands2[z][j + 1] = hands2[z][j]
                j -= 1
            hands2[z][j + 1] = key


a = []
for x in hands2:
    if len(hands2[x]) > 0:
        a = a + hands2[x]
# a.reverse()

for n, h in enumerate(a):
    print(n + 1, h, scores[hands.index(h)], (n + 1) * scores[hands.index(h)])
    solution_1 += (n + 1) * scores[hands.index(h)]


# PART 2
ranking = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
hands3 = {key: [] for key in ["High", "One", "Two", "Three", "Full", "Four", "Five"]}
for x in hands:
    c = Counter(x)
    t = sorted([c[y] for y in list(c)], reverse=True)
    if "J" not in x:
        # print(x)
        if len(t) == 1:
            hands3["Five"].append(x)
        elif t[0] == 4:
            hands3["Four"].append(x)
        elif t[0] == 3 and t[1] == 2:
            hands3["Full"].append(x)
        elif t[0] == 3:
            hands3["Three"].append(x)
        elif t[0] == 2 and t[1] == 2:
            hands3["Two"].append(x)
        elif len(t) == 4:
            hands3["One"].append(x)
        elif len(t) == 5:
            hands3["High"].append(x)
    else:  # ABBCDJ
        js = c["J"]
        if js == 1:
            if t[0] == 4:
                hands3["Five"].append(x)
            elif t[0] == 3:
                hands3["Four"].append(x)
            elif t[0] == 2 and t[1] == 2:
                hands3["Full"].append(x)
            elif len(t) == 4:
                hands3["Three"].append(x)
            elif len(t) == 5:
                hands3["One"].append(x)
        elif js == 2:
            if t[0] == 3 and t[1] == 2:
                hands3["Five"].append(x)
            elif t[0] == 2 and t[1] == 2:
                hands3["Four"].append(x)
            elif len(t) == 4:
                hands3["Three"].append(x)
        elif js == 3:
            if t[0] == 3 and t[1] == 2:
                hands3["Five"].append(x)
            elif t[0] == 3:
                hands3["Four"].append(x)
        else:
            if js >= 4:
                hands3["Five"].append(x)


for z in hands3:
    if len(hands3[z]) > 1:
        for i in range(1, len(hands3[z])):
            key = hands3[z][i]
            j = i - 1
            while j >= 0 and comp(key, hands3[z][j]):
                hands3[z][j + 1] = hands3[z][j]
                j -= 1
            hands3[z][j + 1] = key


a = []
for x in hands3:
    if len(hands3[x]) > 0:
        a = a + hands3[x]
# a.reverse()

for n, h in enumerate(a):
    # print(n + 1, h, scores[hands.index(h)], (n + 1) * scores[hands.index(h)])
    solution_2 += (n + 1) * scores[hands.index(h)]


for x in hands3:
    print(x, hands3[x])

# SOLUTIONS

print("Part One : " + str(solution_1) + "\nPart Two : " + str(solution_2))
