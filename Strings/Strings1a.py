# Exercise 1B: Create a string made of the middle three characters
# Write a program to create a new string made of the middle three characters of an input string.
#
# Given:
#
# Case 1
#
# str1 = "JhonDipPeta"
# Output
#
# Dip
# Case 2
#
# str2 = "JaSonAy"
# Output
#
# Son

def middle_three_char(string):
    middle = len(string) // 2
    middle_char = string[middle-1 : middle +2]
    return middle_char
str1 = middle_three_char("JhonDipPeta")
str2 = middle_three_char("JaSonAy")
print(str1)
print(str2)





