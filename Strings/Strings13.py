# Exercise 13: Split a string on hyphens
# Write a program to split a given string on hyphens and display each substring.
#
# Given:
#
# str1 = Emma-is-a-data-scientist
# Expected Output:
#
# Displaying each substring
#
# Emma
# is
# a
# data
# scientist

def spli_string(str1):
    result = str1.split("-")
    Display = ""
    for i in result:
        Display += str(i)+"\n"
    return Display
str1 = "Emma-is-a-data-scientist"
solution = spli_string(str1)
print(solution)
