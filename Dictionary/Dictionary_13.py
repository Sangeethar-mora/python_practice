# Exercise 13: Check if a value exists in a dictionary
# While we know how to check for a key’s presence in a dictionary, it’s sometimes necessary to determine if a specific value exists.
#
# Write a Python program to check if the value 200 is present in the provided dictionary.
#
# Given:
#
# sample_dict = {'a': 100, 'b': 200, 'c': 300}
# Expected output:
#
# 200 present in a dict

sample_dict = {'a': 100, 'b': 200, 'c': 300}

if 200 in sample_dict.values():
    print("200 present in dict")
else:
    print("200 not in dict")

