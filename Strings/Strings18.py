# Exercise 18: Replace each special symbol with # in the following string
# Given:
#
# str1 = '/*Jon is @developer & musician!!'
# Expected Output:
#
# ##Jon is #developer # musician##

def replace_special_symbol(str1):
    wrd = ""
    for i in str1:
        if i in ["/","@","*","!","&"]:
            wrd += "#"
        else:
            wrd += i
    return wrd
str1 = '/*Jon is @developer & musician!!'
print(replace_special_symbol(str1))
