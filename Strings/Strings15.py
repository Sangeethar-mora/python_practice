# Exercise 15: Remove special symbols / punctuation from a string
# Given:
#
# str1 = "/*Jon is @developer & musician"
# Expected Output:
#
# "Jon is developer musician"

def remove_special_symbols(str1):
    wrd = ""
    removed = ""
    for i in str1:
        if i not in ["&","*","/","@"]:
            wrd+=i
    return wrd
str1 = "/*Jon is @developer & musician"
result = remove_special_symbols(str1)
print(result)

