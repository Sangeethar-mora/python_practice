# Exercise 14: List Comprehension for Numbers
# Use list comprehension to create a new list containing only the numbers from a given list.
#
# Given:
#
# my_list = [1, 2, 3, 'Jessa', 4, 5, 'Kelly', 'Jhon', 6]
# Expected Output:
#
# [1, 2, 3, 4, 5, 6]

def list_comprehension_for_numbers(my_list):
    number_list = []
    for i in my_list:
        if isinstance(i, int):
            number_list.append(i)
    return number_list
my_list = [1, 2, 3, 'Jessa', 4, 5, 'Kelly', 'Jhon', 6]
print(list_comprehension_for_numbers(my_list))

