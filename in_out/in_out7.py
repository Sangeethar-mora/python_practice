# Exercise 7: Accept any three string from one input() call
# Write a program to take three names as input from the user in a single call to the input() function.
#
# See: Get multiple inputs from a user in one line
#
# Expected Output
#
# Enter three string Emma Jessa Kelly
# Name1: Emma
# Name2: Jessa
# Name3: Kelly

Name1, Name2, Name3 = input("enter three strings: ").split()

print("Name1:", Name1)
print("Name2:", Name2)
print("Name3:", Name3)
