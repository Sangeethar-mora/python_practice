# Exercise 2: Perform List Manipulation
# Given:
#
# my_list = [10, 20, 30, 40, 50]
# Perform following list manipulation operations on given list
#
# Change Element: Change the second element of a list to 200 and print the updated list.
# Append Element: Add 600 o the end of a list and print the new list.
# Insert Element: Insert 300 at the third position (index 2) of a list and print the result.
# Remove Element (by value): Remove 600 from the list and print the list.
# Remove Element (by index): Remove the element at index 0 from the list print the list.
# Expected Output:
#
# Initial list: [10, 20, 30, 40, 50]
#
# After changing second element: [10, 200, 30, 40, 50]
# List after appending 600: [10, 200, 30, 40, 50, 600]
# List after inserting 300 at index 2: [10, 200, 300, 30, 40, 50, 600]
# List after removing 600 (by value): [10, 200, 300, 30, 40, 50]
# List after removing element at index 0: [200, 300, 30, 40, 50]

def perform_list_manipulations(my_list):
    my_list[1] = 200
    print("After changing second element: ",my_list)
    my_list.append(600)
    print("List after appending 600: ",my_list)
    my_list.insert(2, 300)
    print("List after inserting 300 at index 2: ",my_list)
    my_list.remove(600)
    print("List after removing 600 (by value): ",my_list)
    my_list.pop(0)
    print("List after removing element at index 0: ",my_list)
my_list = [10, 20, 30, 40, 50]
perform_list_manipulations(my_list)
