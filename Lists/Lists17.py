# Exercise 17: Concatenate two lists index-wise
# Write a program to add two lists index-wise. Create a new list that contains the 0th index item from both the list, then the 1st index item, and so on till the last element. any leftover items will get added at the end of the new list.
#
# Given:
#
# list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]
# Expected output:
#
# ['My', 'name', 'is', 'Kelly']

def concatenate_two_lists_index_wise(list1, list2):
    list_after_concatiniation = []
    for i in range(0, len(list1)):
        list_after_concatiniation.append(list1[i]+list2[i])
    return list_after_concatiniation
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
print(concatenate_two_lists_index_wise(list1, list2))

