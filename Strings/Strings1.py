# Exercise 1A: Create a string made of the first, middle and last character
# Write a program to create a new string made of an input string’s first, middle, and last character.
#
# Given:
#
# str1 = "James"
# Expected Output:
#
# Jms
str1 = "James"

for i in range(len(str1)):
    if i % 2 == 0:
        print(str1[i],end = "")

######### using functions ########

def even_char(str1):
    result = ""
    for i in range(len(str1)):
        if i % 2 == 0:
            result+=str1[i]
    return result
print(even_char("James"))
