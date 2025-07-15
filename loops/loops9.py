# Exercise 9: Display numbers from -10 to -1 using for loop
# Expected output:
#
# -10
# -9
# -8
# -7
# -6
# -5
# -4
# -3
# -2
# -1

for i in range(-10,0,1):
    print(i)

####### using functions ######

def disply_numbers():
    result = ""
    for numbers in range(-10, 0, 1):
        result += str(numbers)+"\n"
    return result
print(disply_numbers())
