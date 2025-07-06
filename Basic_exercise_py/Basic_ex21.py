# Exercise 21: Check if a user-entered string contains any digits using a for loop
# Expected Output:
#
# Enter a string: Pynative123Python
# The string contains at least one digit.
#
# Enter a string: PYnative
# The string does not contain any digits.

input_string = input("Enter a string: ")

d = []

for i in input_string:
    if i.isdigit():
        d+=i
if d:
    print("The string contains at least one digit.")
else:
    print("The string does not contain any digits.")

