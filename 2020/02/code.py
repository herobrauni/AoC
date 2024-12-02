# Advent of code Year 2020 Day 2 solution
# Author = brauni
# Date = 2021-12-01

# with open(os.getcwd() + "\\2020\\02\\example.txt", 'r') as f:
with open(os.getcwd() + "\\2020\\02\\input.txt", "r") as f:
    # input = f.read()
    # input = input.split("\n")
    # input = []
    # for line in f.readlines():
    # input.append(int(line))
    # input = [int(line) for line in f.readlines()]
    input = [line for line in f.readlines()]

"""
print(input)
"""


# PART 1
with open(os.getcwd() + "\\2020\\02\\input.txt", "r") as f:
    solution_1 = [
        (
            lambda line: True
            if (lambda line: line.split())(line)[2].count(
                (lambda line: line.split())(line)[1][0]
            )
            >= int(
                (lambda line: (lambda line: line.split())(line)[0].split("-"))(line)[0]
            )
            and (lambda line: line.split())(line)[2].count(
                (lambda line: line.split())(line)[1][0]
            )
            <= int(
                (lambda line: (lambda line: line.split())(line)[0].split("-"))(line)[1]
            )
            else False
        )(line)
        for line in f.readlines()
    ].count(True)


print("Part One : " + str(solution_1))


# PART 2
solution_2 = 0
with open(os.getcwd() + "\\2020\\02\\input.txt", "r") as pwlist:
    for line in pwlist.readlines():
        x, y, z, l = (
            int(line.split()[0].split("-")[0]),
            int(line.split()[0].split("-")[1]),
            line.split()[2],
            line.split()[1][0],
        )
        if (z[x - 1] == l) != (z[y - 1] == l):
            solution_2 = solution_2 + 1

print("Part Two : " + str(solution_2))
