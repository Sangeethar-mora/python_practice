# Exercise 11: Create a dictionary by extracting the keys from a given dictionary
# Write a Python program to create a new dictionary by extracting the mentioned keys from the below dictionary.
#
# Given dictionary:
#
# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"}
#
# # Keys to extract
# keys = ["name", "salary"]
# Expected output:
#
# {'name': 'Kelly', 'salary': 8000}

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

keys_ext = ["name", "salary"]
dict2 = {}

for i in keys_ext:
    if i in sample_dict:
        dict2[i] = sample_dict[i]

print(dict2)
