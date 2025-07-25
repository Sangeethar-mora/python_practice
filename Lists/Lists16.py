# Exercise 16: Flatten Nested List
# Write a function to flatten a list of lists into a single, non-nested list. (e.g., [[1, 2], [3, 4]] becomes [1, 2, 3, 4]).
#
# Given:
#
# list_of_lists = [[1, 2], [3, 4], [5, 6, 7]]
# Expected Output:
#
# [1, 2, 3, 4, 5, 6, 7]

def Flatten_Nested_list(list_of_list):
    Flattend_list = []
    for i in list_of_list:
        if isinstance(i, list):
            for j in i:
                Flattend_list.append(j)
    return Flattend_list
list_of_lists = [[1, 2], [3, 4], [5, 6, 7]]
print(Flatten_Nested_list(list_of_lists))
