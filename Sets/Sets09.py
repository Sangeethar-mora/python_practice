# Exercise 9: Check Subset
# Check if set1 is a subset of set2.
# Write a code to return True if every element in the subset_set is also present in the main_set.
#
# Given:
#
# subset_set = {10, 20}
# main_set = {10, 20, 30, 40}
# Expected Output:
#
# True

main_set = {10, 20, 30, 40}
subset_set = {10, 20}

if subset_set.issubset(main_set):
    print(True)
else:
    print(False)
