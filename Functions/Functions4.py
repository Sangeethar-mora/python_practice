# Exercise 4: Create a function with a default argument
# Write a program to create a function show_employee() with the following specifications:
#
# It should accept the employee’s name and salary.
# It should display both the name and salary.
# If the salary is not provided in the function call, it should default to 9000.
# See: Default arguments in function
#
# Given:
#
# showEmployee("Ben", 12000)
# showEmployee("Jessa")
# Expected output:
#
# Name: Ben salary: 12000
# Name: Jessa salary: 9000

def show_employee(name, salary = 9000):
    return name, salary
print(show_employee("Ben", 12000))
print(show_employee("jessa"))
