# Exercise 12: Find the last position of a given substring
# Write a program to find the last position of a substring “Emma” in a given string.
#
# Given:
#
# str1 = "Emma is a data scientist who knows Python. Emma works at google."
# Expected Output:
#
# Last occurrence of Emma starts at index 43

def position_of_string(str1):
    find_word = "emma"
    for i in str1:
        if find_word in str1:
            return True
    else:
        return False
str1 = "Emma is a data scientist who knows Python. Emma works at google."
index_position = position_of_string(str1)
print(index_position)

