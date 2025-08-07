# Exercise 12: Set Symmetric Difference Update
# Write a program to update set1 by adding items from set2 that are not common to both sets.
#
# Given:
#
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# Expected output:
#
# {70, 10, 20, 60}

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

set1.symmetric_difference_update(set2)
print(set1)
