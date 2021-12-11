# remove all occurances of value N from 2d List
res = [[ele for ele in sub if ele != N] for sub in test_list]

# remove all occurances of value N from 2d List
for sub in test_list:
    sub[:] = [ele for ele in sub if ele != N]

# Get counts of all values in 1d List
common = Counter([row[i] for row in input])

# use deepcopy for nested lists, otherwise will be a shallow copy
x = copy.deepcopy(y)

# deduplicate list
list_a = list(dict.fromkeys(list_a))

# returns a list with only the counters of the numbers in the specified range
# so [0] is the count of 0, [1] is the count of 1, etc.
[input.count(i) for i in range(9)]

# removes the element on index i from the list and returns the element
# can be used to remove the first element from a list and add it at the end with .append()
list.pop(i)


# For Else loop -> else runs only if no break is called in the loop
for line in input:
    if line == "":
        break
else:
    print(line)
