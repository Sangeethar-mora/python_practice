# Exercise 11: Function Returning Tuple
# Write a function get_min_max(numbers) that takes a list of numbers and returns a tuple containing the minimum and maximum number.
#
# Given:
#
# def get_min_max(numbers):
#     # Write your code here
#
# # Test the function
# my_numbers = [10, 5, 20, 2, 15]
# min_max_values = get_min_max(my_numbers)
# print(f"Original numbers: {my_numbers}")
# print(f"Minimum and maximum values: {min_max_values}")

def get_min_max(numbers):
    min_max_values = []
    min_max_values.append(min(numbers))
    min_max_values.append(max(numbers))
    return tuple(min_max_values)

my_numbers = [10, 5, 20, 2, 15]
min_max_values = get_min_max(my_numbers)
print(f"Original numbers: {my_numbers}")
print(f"Minimum and maximum values: {min_max_values}")








