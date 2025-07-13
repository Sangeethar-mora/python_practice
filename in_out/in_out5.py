# Exercise 5: Accept a list of 5 float numbers as an input from the user
# Refer:
#
# Take list as a input in Python.
# Python list
# Expected Output:
#
# [78.6, 78.6, 85.3, 1.2, 3.5]

# using while loop instead of for loop
numbers = []
n = 0
while n < 5:
    num = float(input(f"Enter number{n}"))
    numbers.append(num)
    n = n+1
print("User List:", numbers)

# using for loop
numbers = []
for i in range(0,5):
    num = float(input(f"Enter number{i}"))
    numbers.append(num)
    n = n+1
print("User List:", numbers)

############### using functions ###########

# method 1

def list_float_numbers():
    numbers = []

    n = 0

    while n < 5:
        num = float(input(f"Enter number{n}: "))
        numbers.append(num)
        n = n+1
    return numbers
print(list_float_numbers())

# method 2

def list_float_numbers():
    numbers = []
    for i in range(0,5):
        num = float(input(f"Enter number{i}: "))
        numbers.append(num)
        n = n+1
    return numbers
print(list_float_numbers())
