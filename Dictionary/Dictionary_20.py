# Exercise 20: Check if All Values are Unique
# Write a function that takes a dictionary and returns True if all values in the dictionary are unique, False otherwise.
#
# Given:
#
# dict1 = {'a': 1, 'b': 2, 'c': 3}             # All values unique
# dict2 = {'x': 10, 'y': 20, 'z': 10}          # Value 10 is duplicated
# dict3 = {} # Empty dictionary (all values are vacuously unique)
# Expected Output:
#
# Dictionary: {'a': 1, 'b': 2, 'c': 3} -> All values unique? True
# Dictionary: {'x': 10, 'y': 20, 'z': 10} -> All values unique? False
# Dictionary: {} -> All values unique? True

def check_unique_values(dict_li):
    uni_set = set(dict_li.values())
    if len(dict_li) == len(uni_set):
        return f"{dict_li} -> All values unique? {True}"
    else:
        return f"{dict_li} -> All values unique? {False}"

dict1 = {'a': 1, 'b': 2, 'c': 3}             # All values unique
dict2 = {'x': 10, 'y': 20, 'z': 10}          # Value 10 is duplicated
dict3 = {}
print(check_unique_values(dict1))
print(check_unique_values(dict2))
print(check_unique_values(dict3))
