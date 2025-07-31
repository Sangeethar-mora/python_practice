# Exercise 12: Delete a list of keys from a dictionary
# Given:
#
# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"
# }
#
# # Keys to remove
# keys = ["name", "salary"]
# Expected output:
#
# {'city': 'New york', 'age': 25}

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

keys_remove = ["name", "salary"]

for i in keys_remove:
        sample_dict.pop(i)
print(sample_dict)
