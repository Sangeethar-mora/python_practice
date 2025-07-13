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
############################## using functions #################
# method one

def rm_char_from_string(string, num_to_rm):
    return string[num_to_rm: ]
print(rm_char_from_string('pynative', 4))

# Second method

def rm_char_from_string(string, num_to_rm):
    for i in range(len(string)):
        if i >= num_to_rm:
            print(string[i],end="")
rm_char_from_string('pynative', 2)

#third method

def rm_char_from_string(string, num_to_rm):
    for i in string[num_to_rm:]:
         print(i,end="")
rm_char_from_string('pynative', 4)
