# Exercise 17: Invert Dictionary
# Write a code to swap keys and values in a dictionary. Assume all values are unique
#
# Given:
#
# original_dict1 = {'a': 1, 'b': 2, 'c': 3}
# Expected Output:
#
# Original dictionary 1: {'a': 1, 'b': 2, 'c': 3}
# Inverted dictionary 1: {1: 'a', 2: 'b', 3: 'c'}


original_dict1 = {'a': 1, 'b': 2, 'c': 3}
print("Original dict",original_dict1)

inverted_dict = {}

for i, j in original_dict1.items():
    inverted_dict[j] = i
print(inverted_dict)


