# Exercise 6: Create a mixed String using the following rules
# Given two strings, s1 and s2. Write a program to create a new string s3 made of the first char of s1, then the last char of s2, Next, the second char of s1 and second last char of s2, and so on. Any leftover chars go at the end of the result.
#
# Given:
#
# s1 = "Abc"
# s2 = "Xyz"
# Expected Output:
#
# AzbycX

def mixed_string(s1, s2):
    s3 = ""
    str1 = len(s1)//2
    str2 = len(s2)//2
    s3 += s1[0]+s2[-1] + s1[str1] + s2[str2] +s1[-1] +s2[0]
    return s3count = 0
s1 = "Abc"
s2 = "Xyz"
print(mixed_string(s1, s2))

