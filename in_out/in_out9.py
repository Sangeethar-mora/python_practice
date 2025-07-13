# Exercise 9: Check File is Empty or Not
# Write a program to check if the given file is empty or not

# here by checking the stat can get the detatails of time,size and so on.
import os
size = os.stat("test.txt").st_size
if size == 0:
    print('file is empty')
else:
    print("not empty")

############# using functions ############

import os

def file_size():
    size = os.stat("test.txt").st_size
    if size == 0:
        return 'file is empty'
    else:
        return "not empty"

print(file_size())
