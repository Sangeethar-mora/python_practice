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
# using slicing method
for i in string[::2]:
    print(i)
######3 rd method #######
# using count method
c = 1
for i in string:
    if c%2 != 0:
        print(i)
    c = c+1
########## using functions ########

def odd_caracters(string):
    for char in range(len(string)):
        if char % 2 == 0:
            print(string[char])
odd_caracters('pynative')

######## second method in functions ##

def odd_characters(string):
    for i in string[::2]:
        print(i)
odd_characters('pynative')

######## third method ######

def odd_characters(string):
    c = 1
    for i in string:
        if c%2 != 0:
            print(i)
        c = c+1
odd_characters('pynative')













