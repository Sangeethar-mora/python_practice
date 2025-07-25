# Exercise 13: Remove all occurrences of a specific item from a list
# Given a Python list, write a program to remove all occurrences of item 20.
#
# Given:
#
# list1 = [5, 20, 15, 20, 25, 50, 20]
# Expected output:
#
# [5, 15, 25, 50]

def remove_all_occurrence_of_item(list1):
    for i in list1:
        if i == 20:
            list1.remove(20)
    return list1
list2 = [5, 20, 15, 20, 25, 50, 20]
print(remove_all_occurrence_of_item(list2))
