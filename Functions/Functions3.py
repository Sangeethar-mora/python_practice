# Exercise 3: Return multiple values from a function
# Write a function calculation() that accepts two variables and calculates both their addition and subtraction. The function should then return both the sum and the difference in a single return statement.
#
# Given:
#
# def calculation(a, b):
#     # Your Code
#
# res = calculation(40, 10)
# print(res)
# Expected Output
#
# 50, 30

def calculations(a, b):
    addition = a + b
    subractions = a - b
    return addition, subractions
res = calculations(40, 10)
print(res)
