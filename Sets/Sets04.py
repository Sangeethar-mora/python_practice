# Exercise 4: Difference of Sets
# Find the difference (set1 - set2). Write a code to returns a new set containing elements that are present in set1 but not in set2.
#
# Given:
#
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# Expected Output:
#
# {10, 20}

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

difference_set = set1.difference(set2)
print(difference_set)
