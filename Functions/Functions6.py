# Exercise 6: Create a recursive function
# Write a program to create a recursive function that calculates the sum of numbers from 0 to 10.
#
# A recursive function is a function that calls itself repeatedly.
#
# Expected Output:
#
# 55

def calculate_sum(number):
    if number == 0:
        return 0
    return number + calculate_sum(number - 1)

print(calculate_sum(10))


