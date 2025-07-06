# Exercise 3: Print characters present at an even index number
# Write a Python code to accept a string from the user and display characters present at an even index number.
#
# For example, str = "PYnative". so your code should display ‘P’, ‘n’, ‘t’, ‘v’.
#
# Expected Output:
#
# Orginal String is  PYnative
# Printing only even index chars
# P
# n
# t

string = input("original string is: ")
print("printing only even index characters")
for i in range(len(string)):
    if i%2 == 0:
        print(string[i])
#second method
for i in string[::2]:
    print(i)
######3 rd method #######
c = 1
for i in string:
    if c%2 != 0:
        print(i)
    c = c+1













