# Exercise 7: String characters balance Test
# Write a program to check if two strings are balanced. For example, strings s1 and s2 are balanced if all the characters in the s1 are present in s2. The character’s position doesn’t matter.
#
# Given:
#
# Case 1:
#
# s1 = "Yn"
# s2 = "PYnative"
# Expected Output:
#
# True
# Case 2:
#
# s1 = "Ynf"
# s2 = "PYnative"
# Expected Output:
#
# False

s1 = "Yn"
s2 = "PYnative"
# def character_balance(s1, s2):

for i in s2:
    if s1 not in s2:
        print(False)
else:
    print(True)
########################
def character_balance(s1, s2):
    for char in s2:
        if s1 in s2:
            return True
    else:
        return False
s1 = "Yn"
s2 = "PYnative"
result1 = character_balance(s1, s2)

s3 = "Ynf"
s4 = "PYnative"
result2 = character_balance(s3, s4)

print(result1)
print(result2)

