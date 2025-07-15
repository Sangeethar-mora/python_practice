# Exercise 3: Calculate sum of all numbers from 1 to a given number
# Write a Python program to accept a number from a user and calculate the sum of all numbers from 1 to a given number
#
# For example, if the user entered 10, the output should be 55 (1+2+3+4+5+6+7+8+9+10)
#
# Expected Output:
#
# Enter number 10
# Sum is:  55

n = int(input("Enter a number: "))
total = n * (n + 1) // 2
print(f"The sum of numbers from 1 to {n} is {total}")

############### using functions   ###########

def calliculate_sum_of_numbers(n):
    total = n * (n + 1) // 2
    return f"The sum of numbers from 1 to {n} is {total}"
n = int(input("Enter a number: "))
print(calliculate_sum_of_numbers(n))
