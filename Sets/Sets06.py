# Exercise 6: Add a list of Elements to a Set
# Given a Python list, write a program to add all of its elements into a given set.
#
# Given:
#
# sample_set = {"Yellow", "Orange", "Black"}
# sample_list = ["Blue", "Green", "Red"]
# Expected output:
#
# Note: Set is unordered.
#
# {'Green', 'Yellow', 'Black', 'Orange', 'Red', 'Blue'}

sample_set = {"Yellow", "Orange", "Black"}
sample_list = ["Blue", "Green", "Red"]

sample_set.update(sample_list)
print(sample_set)
