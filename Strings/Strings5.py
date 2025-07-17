# Exercise 5: Count all letters, digits, and special symbols from a given string
# Given:
#
# str1 = "P@#yn26at^&i5ve"
# Expected Outcome:
#
# Total counts of chars, digits, and symbols
#
# Chars = 8
# Digits = 3
# Symbol = 4

def count_given_string(string):
    count_chars = 0
    count_digits = 0
    count_symbol = 0
    for i in string:
        if i.isalpha():
            count_chars += 1
        elif i.isdigit():
            count_digits+=1
        else:
            count_symbol+=1

    return f"chars: {count_chars}\nDigits: {count_digits} \nSymbol: {count_symbol}"
print(count_given_string("P@#yn26at^&i5ve"))
