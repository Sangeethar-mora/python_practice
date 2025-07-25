# Exercise 22: Extend nested list by adding the sublist
# You have given a nested list. Write a program to extend it by adding the sublist ["h", "i", "j"] in such a way that it will look like the following list.
#
# Given List:
#
# list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
#
# # sub list to add
# sub_list = ["h", "i", "j"]
# Expected Output:
#
# ['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n']

def Extend_nested_list(list1):
    sub_list = ["h", "i", "j"]
    list1[2][1][2].extend(sub_list)
    return list1

list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
print(Extend_nested_list(list1))
