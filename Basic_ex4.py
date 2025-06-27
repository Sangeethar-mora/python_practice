# Exercise 4: Remove first n characters from a string
# Write a Python code to remove characters from a string from 0 to n and return a new string.


my_string = str(input("enter the string"))
int_rm = int(input("enter the no"))
print(my_string[int_rm: ])
######################################
for i in my_string[int_rm:]:
    print(i,end="")
#####################################
for i in range(len(my_string)):
    if i >= int_rm:
        print(my_string[i],end="")
