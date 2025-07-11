# Exercise 13: Find the factorial of a given number
# Write a Python program to use for loop to find the factorial of a given number.
#
# The factorial (symbol: !) means multiplying all numbers from the chosen number down to 1.
#
# For example, a factorial of 5! is 5 × 4 × 3 × 2 × 1 = 120
#
# Expected output:
#
# 120
factorial = 1
num = int(input("Enter the number to calculate factorial:"))
for i in range(1, num+1):
    factorial  = factorial*i
print(factorial)
