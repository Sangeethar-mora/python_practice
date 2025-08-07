# Exercise 13: Set Intersection Update
# Write a code to remove items from set1 that are not present in set2.
#
# Given:
#
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# Expected output:
#
# {40, 50, 30}

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

set2.intersection_update(set1)
print(set2)
