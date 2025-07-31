# Exercise 18: Sort Dictionary by Keys
# Sort a dictionary by its keys and print the sorted dictionary (as an OrderedDict or by converting to a list of tuples).
#
# Given:
#
# my_dict = {'apple': 3, 'zebra': 1, 'banana': 2, 'cat': 4}
# Expected Output:
#
# Original dictionary: {'apple': 3, 'zebra': 1, 'banana': 2, 'cat': 4}
#
# Sorted by keys (as OrderedDict):
# OrderedDict([('apple', 3), ('banana', 2), ('cat', 4), ('zebra', 1)])

my_dict = {'apple': 3, 'zebra': 1, 'banana': 2, 'cat': 4}
ordered_dict = {}
sorted_keys = my_dict.items()
print(sorted(sorted_keys))






