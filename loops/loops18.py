# Exercise 18: Print the following pattern
# Write a program to print the following start pattern using the for loop
#
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

for i in range(1,6):
    print(("*"+" ")*i)
for i in range(4, 0, -1):
    print("* " *i)

def pattern():
    result = ""
    for i in range(1, 6):
        result += (("*"+" ")*i)+"\n"
    for j in range(4, 0, -1):
        result += ("* " *j)+"\n"
    return result
print(pattern())
