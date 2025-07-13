# Exercise 22: Capitalize the first letter of each word in a string
# Expected Output:
#
# str1 = "pynative.com is for python lovers"
# # Output Pynative.com Is For Python Lovers
####################################################
# method 1
my_string = "pynative.com is for python lovers"
capital_string = my_string.title()
print(capital_string)

# method 2

string = my_string.split(" ")
for i in string:
    print(i.capitalize(),end = " ")

########## using functions #############

# method 1

def capitalize_letters(string):
    capital_string = string.title()
    return capital_string
result = capitalize_letters("pynative.com is for python lovers")
print(result)

# method 2

def capitalize_letters(string):
    my_string = string.split(" ")
    result = ""
    for i in my_string:
        result+=i.capitalize()+" "
    return result
string = "pynative.com is for python lovers"
print(capitalize_letters(string))





