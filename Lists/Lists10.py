# Exercise 10: Combine two lists
# Combine given two lists into a single list and print it.
#
# Given:
#
# list_a = [1, 2]
# list_b = [3, 4]
# Expected Output:
#
# [1, 2, 3, 4]

def combine_two_list(list_a, list_b):
    my_list = list_a + list_b
    return my_list
list_a = [1, 2]
list_b = [3, 4]
print(combine_two_list(list_a, list_b))
