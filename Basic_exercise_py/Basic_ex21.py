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

############## using functions ##################

def contains_digit(string):
    digits = []
    for char in string:
        if char.isdigit():
            digits+=char

    if digits:
        return "The string contains at least one digit."
    else:
        return "The string does not contain any digits."

user_input = input("Enter a string: ")
print(contains_digit(user_input))

