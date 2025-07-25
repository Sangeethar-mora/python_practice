# Exercise 12: Remove Duplicates from list
# Write a function that takes a list with duplicate elements and returns a new list with only unique elements.
#
# Given: list_with_duplicates = [1, 2, 2, 3, 1, 4, 5, 4]
#
# Expected Output:
#
# [1, 2, 3, 4, 5]
def remove_Duplicates(list_with_duplicates):
    unique_list = list(set(list_with_duplicates))
    return f"List without duplicates: {unique_list}"
list_with_duplicates = [1, 2, 2, 3, 1, 4, 5, 4]
print(remove_Duplicates(list_with_duplicates))
