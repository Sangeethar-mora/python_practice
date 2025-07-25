# Exercise 9: Create a copy of a list
# Create a copy of a list [10, 20, 30] and modify the copy.
# Print both the original and the copied list to demonstrate they are independent.

def copy_list(my_list):
    original_list = my_list.copy()
    my_list[2] = 50
    return f"copy list: {original_list}\nOrginal list: {my_list}"
my_list = [10, 20, 30, 40]
print(copy_list(my_list))
