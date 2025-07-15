# Exercise 2: Print the following pattern
# Write a Python code to print the following number pattern using a loop.
#
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5


num = ""
for i in range(1,6):
    num+=str(i)+" "
    print(num)
################ using functions ############
def pattern():
    num = ""
    result = ""
    for i in range(1,6):
        num+=str(i)+" "
        result+=num+"\n"
    return result
print(pattern())
