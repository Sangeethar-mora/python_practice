# Exercise 13: Display Right-Aligned Output
# Ask the user for a word and a number. Print the word right-aligned in a field of width 20, followed by the number.
#
# Expected Output:
#
# Enter a word:  PYnative
# Enter a number:  29
#             PYnative29
# used word is a variable (assumed to be a string).
#
# :>20 means right-align the text in a field of width 20 characters.
# :<20 means left-align the text
# :^20 means middle-align the text


word = input("enter the word: ")
number = input("enter the number: ")

print(f"{word:>20}{number}")
