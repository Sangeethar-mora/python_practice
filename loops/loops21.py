# Exercise 21: Flatten a nested list using loops
# Write a program to flatten a nested list using loops.
#
# Given:
#
# nested_list = [1, [2, 3], [4, 5, 6], 7, [8, 9]]
#
# # write function 'flatten_list' to flatten a nested list
# flattened = flatten_list(nested_list)
# print("Flattened list:", flattened)
#
# # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
nested_list = [1, [2, 3], [4, 5, 6], 7, [8, 9]]
flattend = []
for i in nested_list:
    if isinstance(i, list):
        for j in i:
            flattend.append(j)
    else:
        if isinstance(i, int):
            flattend.append(i)
print(flattend)



