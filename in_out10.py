# Exercise 10: Read Line Number 4 from File
# See:
#
# Read Specific Lines From a File in Python
# Python read file
# Create a test.txt file and add the below content to it.
#
# test.txt file:
#
# line1
# line2
# line3
# line4
# line5
# line6
# line7

with open("test.txt","r") as file:
    filr_r = file.readlines()
    print(filr_r[3])


