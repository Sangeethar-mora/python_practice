# Exercise 15: Padding with Zeros
# Ask the user for a number. Print this number padded with leading zeros to a width of 5.
#
# For example, if the input is 12, the output should be “00012“
# The .zfill() method in Python is used to pad a numeric string on
# the left with zeros so that it reaches a specified length.

user_number = input("enter the number")
print(f"{user_number:0>5}")

number_str = input("Enter a number: ")
padded_number = number_str.zfill(5)
print(padded_number)

user_number = input("Enter the number: ")
padded_number = ("00000" + user_number)[-5:]
print(padded_number)
