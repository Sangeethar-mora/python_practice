# Exercise 3: Create a new string made of the first, middle, and last characters of each input string
# Given two strings, s1 and s2, write a program to return a new string made of s1 and s2’s first, middle, and last characters.
#
# Given:
#
# s1 = "America"
# s2 = "Japan"
# Expected Output:
#
# AJrpan
s1 = "America"
s2 = "Japan"
def new_string(s1,s2):
    result = ""
    middle1 = len(s1)//2
    middle2 = len(s2)//2
    result += s1[0]+s2[0]+s1[middle1]+s2[middle2]+s1[-1]+s2[-1]
    return result
s1 = "America"
s2 = "Japan"
print(new_string(s1, s2))
