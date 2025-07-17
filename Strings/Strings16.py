# Exercise 16: Removal all characters from a string except integers
# Given:
#
# str1 = 'I am 25 years and 10 months old'
# Expected Output:
#
# 2510

def remove_all_char(str1):
    digits = ""
    for i in str1:
        if i.isdigit():
            digits+=str(i)
    return digits
str1 = 'I am 25 years and 10 months old'
removed = remove_all_char(str1)
print(removed)
