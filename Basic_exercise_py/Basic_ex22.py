# Exercise 22: Capitalize the first letter of each word in a string
# Expected Output:
#
# str1 = "pynative.com is for python lovers"
# # Output Pynative.com Is For Python Lovers

my_string = "pynative.com is for python lovers"
capital_string = my_string.title()
print(capital_string)
##############################

string = my_string.split(" ")
for i in string:
    print(i.capitalize(),end = " ")


