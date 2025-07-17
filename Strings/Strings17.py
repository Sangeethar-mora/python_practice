# Exercise 17: Find words with both alphabets and numbers
# Write a program to find words with both alphabets and numbers from an input string.
#
# Given:
#
# str1 = "Emma25 is Data scientist50 and AI Expert"
# Expected Output:
#
# Emma25
# scientist50

def word_alpabets_numbers(str1):
    split_str = str1.split()
    wrd_special = ""
    wrd = ""
    for i in split_str:
        if i.isalpha():
            wrd+=i+" "
        else:
            wrd_special += i+"\n"
    return wrd_special

str1 = "Emma25 is Data scientist50 and AI Expert"
sort = word_alpabets_numbers(str1)
print(sort)
