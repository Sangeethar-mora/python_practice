# Exercise 11: Get each digit from a number in the reverse order.
# For example, If the given integer number is 7536, the output shall be “6 3 5 7“, with a space separating the digits.
#
# Given:
#
# number = 7536
# # Output 6 3 5 7

num1 = input("given integer ")
result = num1[: : -1]
for i in result:
    print(i, end = " ")

##################################
num = 4654

while num > 0:
    rm = num%10
    num = num//10
    print(rm,end = " ")

################ using functions #################

number = 7536
def reverse_number():
    result = ""
    global number
    while number > 0:
        rm = number % 10
        number = number // 10
        result+= str(rm) + " "
    return result

answer = reverse_number()

print(answer)

