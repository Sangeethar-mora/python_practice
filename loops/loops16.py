# Exercise 16: Calculate the cube of all numbers from 1 to a given number
# Write a Python program to print the cube of all numbers from 1 to a given number
#
# Given:
#
# input_number = 6
#
# Expected output:
#
# Current Number is : 1  and the cube is 1
# Current Number is : 2  and the cube is 8
# Current Number is : 3  and the cube is 27
# Current Number is : 4  and the cube is 64
# Current Number is : 5  and the cube is 125
# Current Number is : 6  and the cube is 216
num = int(input("give the number to get the range of the cube numbers"))
for i in range(1, num+1):
    cube = i**3
    print(f"current Number is : {i} and the cube is {cube}")

############## using functions ###########

def calculate_cube(given_number):
    result = ""
    for i in range(1, given_number+1):
        cube = i ** 3
        result += f"current Number is : {i} and the cube is {cube}"+"\n"
    return result
given_number = int(input("give the number to get the range of the cube numbers"))
print(calculate_cube(given_number))
