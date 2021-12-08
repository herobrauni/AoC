# Advent of code Year 2020 Day 4 solution
# Author = brauni
# Date = 2021-12-01
import re
import os

# with open(os.getcwd() + "\\2020\\04\\example.txt", 'r') as f:
with open(os.getcwd() + "\\2020\\04\\input.txt", 'r') as f:
    input = f.read()
    input = input.split("\n\n")
    # input = []
    # for line in f.readlines():
    # input.append(int(line))
    #input = [int(line) for line in f.readlines()]
    # input = [line for line in f.readlines()]

"""
print(input)
"""


# PART 1
fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

count = 0

for b in input:
    c = 0
    for x in fields:
        if (x in b):
            c += 1
    if (c == 7):
        count += 1

print("Part One : " + str(count))


# PART 2
fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
byr = "byr:(19[2-9][0-9]|200[0-2])"
iyr = "iyr:((201[0-9])|2020)"
eyr = "eyr:((202[0-9])|2030)"
hgt = "hgt:((((1[5-8][0-9])|(19[0-3]))cm)|((59|6[0-9]|7[0-6])in))"
hcl = "hcl:#[0-9|a-f]{6}"
ecl = "ecl:(amb|blu|brn|gry|grn|hzl|oth)"
pid = "pid:[0-9]{9}(\s|$)"

count = 0

for u in input:
    u = u.strip("\n")
    checks = [0, 0, 0, 0, 0, 0, 0]
    if (re.search(byr, u)):
        checks[0] += 1
    if (re.search(iyr, u)):
        checks[1] += 1
    if (re.search(eyr, u)):
        checks[2] += 1
    if (re.search(hgt, u)):
        checks[3] += 1
    if (re.search(hcl, u)):
        checks[4] += 1
    if (re.search(ecl, u)):
        checks[5] += 1
    if (re.search(pid, u)):
        checks[6] += 1
    if (sum(checks) == 7):
        count += 1

print("Part Two : " + str(count))
