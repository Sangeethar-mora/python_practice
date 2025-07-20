# Exercise 6: Set Intersection and Removal
# Write a code to find the intersection (common) of two sets and remove those elements from the first set.
#
# See: Python Set
#
# Given:
#
# first_set = {23, 42, 65, 57, 78, 83, 29}
# second_set = {57, 83, 29, 67, 73, 43, 48}
# Expected Output:
#
# Intersection is  {57, 83, 29}
# First Set after removing common element  {65, 42, 78, 23}

def set_intersection_and_removal(first_set, second_set):

    intersection = first_set & second_set
    first_set-=intersection
    return f"Intersection is  {intersection}\nFirst Set after removing common element  {first_set}"

first_set = {23, 42, 65, 57, 78, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}
print(set_intersection_and_removal(first_set, second_set))
