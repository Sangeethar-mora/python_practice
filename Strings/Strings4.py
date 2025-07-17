# Exercise 4: Arrange string characters such that lowercase letters should come first
# Given string contains a combination of the lower and upper case letters. Write a program to arrange the characters of a string so that all lowercase letters should come first.
#
# Given:
#
# str1 = PyNaTive
# Expected Output:
#
# yaivePNT
str1 = "PyNaTive"
res = ""
for i in str1:
    if i.islower():
        res+= i
for i in str1:
    if i.isupper():
        res+= i
print(res)

############ using functions ########

def arrange_characters(string):
    result = ""
    for i in string:
        if i.islower():
            result += i
    for j in string:
        if j.isupper():
            result += j
    return  result
sorted = arrange_characters("PyNaTive")
print(sorted)
