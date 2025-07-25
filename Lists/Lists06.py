# Exercise 6: Find Maximum and Minimum
# Find and print the largest and smallest number in a list [8, 2, 15, 1, 9].
#
# Given:
#
# data = [8, 2, 15, 1, 9]
# Expected Output:
#
# Largest number: 15
# Smallest number: 1

def min_max_list(data):
    return f"Largest number: {max(data)}\nSmallest number: {min(data)}"
data = [8, 2, 15, 1, 9]
print(min_max_list(data))
