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
temp_remove = list(dict.fromkeys(temp_remove))
