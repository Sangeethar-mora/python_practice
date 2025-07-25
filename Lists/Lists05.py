# Exercise 5: Turn every item of a list into its square
# Given a list of numbers. write a program to turn every item of a list into its square.
#
# Given:
#
# numbers = [1, 2, 3, 4, 5, 6, 7]
# Expected output:
#
# [1, 4, 9, 16, 25, 36, 49]

def item_of_list_into_square(numbers):
    my_list = []
    for i in numbers:
        my_list.append(i**2)
    return my_list
numbers = [1, 2, 3, 4, 5, 6, 7]
print(item_of_list_into_square(numbers))
