# Exercise 13: Write a recursive function to calculate the factorial
# Write a recursive function to calculate the factorial of a non-negative integer.

def factorial(number):
    if number == 0:
        return 1
    return number * factorial(number - 1)
number = 5
result = factorial(number)
print(result)
