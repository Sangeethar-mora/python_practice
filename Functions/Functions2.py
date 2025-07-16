# Exercise 2: Create a function with variable length of arguments
# Write a program to create a function func1() that accepts a variable number of arguments and prints each of their values.
#
# Note: Create this function so that it can receive any number of arguments, process them, and display the value of each individual argument.
#
# Read: variable length of arguments in functions
#
# Function call:
#
# # call function with 3 arguments
# func1(20, 40, 60)
#
# # call function with 2 arguments
# func1(80, 100)

def func1(*args):
    result = ""
    for i in args:
        result += str(i)+"\n"
    return result
print("printing values")
print(func1(20, 40, 60))
print("printing values")
print(func1(80, 100))
