# Exercise 1: Perform Basic List Operations
# Given:
#
# my_list = [10, 20, 30, 40, 50]
# Perform following operations on given list
#
# Access Elements: Print the third element.
# List Length: Print the number of elements in the list
# Check if Empty: Write a code to check is list empty.
# Expected Output:
#
# Initial list: [10, 20, 30, 40, 50]
#
# Third item:  30
# Length of the list: 5
# list is not empty

def Basic_lists(my_list):
    if len(my_list) == 0:
        print ("list is empty")
    else:
        print("list is not empty")
    return f"Third item:  {my_list[2]}\nLength of the list: {len(my_list)}"
my_list = [10, 20, 30, 40, 50]
print("Initial list: ",my_list)
print(Basic_lists(my_list))
