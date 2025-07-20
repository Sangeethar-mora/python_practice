# Exercise 2: Remove and add item in a list
# Write a program to remove the item present at index 4 and add it to the 2nd position and at the end of the list.
#
# Given:
#

def remove_and_add_list(list1):
    new = []
    new4 = []
    for i in list1:
        if i != list1[4]:
            new.append(i)
        else:
            new4.append(i)
    return f"List After removing element at index 4\n{new}\nList after Adding element at index 2\n{new[:2]+new4+new[2:]}\nList after Adding element at last\n{new[:2]+new4+new[2:] + new4}"
list1 = [54, 44, 27, 79, 91, 41]
print(remove_and_add_list(list1))
