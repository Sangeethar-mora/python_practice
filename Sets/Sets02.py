# Exercise 2: Union of Sets
# Find the union of set1 and set2. Write a Python program to return a new set with unique items from both sets by removing duplicates.
#
# Given:
#
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# Expected Output:
#
# {70, 40, 10, 50, 20, 60, 30}

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

union_set = set2.union(set1)
print(union_set)
