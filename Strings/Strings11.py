# Exercise 11: Reverse a given string
# Given:
#
# str1 = "PYnative"
# Expected Output:
#
# evitanYP

def reverse_string(str1):
    result = ""
    for i in str1[::-1]:
        result += i
    return result
str1 = "PYnative"
reversed_string = reverse_string(str1)
print(reversed_string)
