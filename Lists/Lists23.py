# Exercise 23: Replace list’s item with new value if found
# You have given a Python list. Write a program to find value 20 in the list, and if it is present, replace it with 200. Only update the first occurrence of an item.
#
# Given:
#
# list1 = [5, 10, 15, 20, 25, 50, 20]
# Expected output:
#
# [5, 10, 15, 200, 25, 50, 20]

def replace_list_item(list1):
    index_replace = list1.index(20)
    list1[index_replace]  = 200
    return list1

list1 = [5, 10, 15, 20, 25, 50, 20]
print(replace_list_item(list1))
