# Exercise 15: Frozen Set
# Create a frozen set from a list.
#
# Given:
#
# my_list = [10, 20, 30]
# Expected Output:
#
# ({10, 20, 30})
my_list = [10, 20, 30]
print(frozenset(set(my_list)))
