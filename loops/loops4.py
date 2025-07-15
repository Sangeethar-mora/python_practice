# Exercise 4: Print multiplication table of a given number
# Given:
#
# num = 2
# Expected output is:
#
# 2
# 4
# 6
# 8
# 10
# 12
# 14
# 16
# 18
# 20
num = 2
for i in range(1,11):
    print(i*num)

####### using functions #######

def multiplication_table(num = 2):
    result = ""
    for i in range(1,11):
        result += f"{i*num}\n"
    return result
print(multiplication_table())
