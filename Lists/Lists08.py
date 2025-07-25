# Exercise 8: Sort a list of numbers
# Sort a given list of numbers in ascending order and print it.
#
# Given: numbers = [5, 2, 8, 1, 9]
#
# Expected Output:
#
# Original list: [5, 2, 8, 1, 9]
# Sorted list: [1, 2, 5, 8, 9]

def sort_list(numbers):
    return f"Original list: {numbers}\nSorted list: {sorted(numbers)}"
numbers = [5, 2, 8, 1, 9]
print(sort_list(numbers))
