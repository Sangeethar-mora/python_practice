# Exercise 22: Find largest and smallest digit in a number
# Write a program in Python identifies the digit with the highest value and the digit with the lowest value within that number.
#
# Input:
#
# num1 = 9876543210
# num2 = -5082
# Output:
#
# Largest digit in 9876543210: 9
# Smallest digit in 987654321: 1
#
# Largest digit in -5082: 8
# Smallest digit in -5082: 0
num1 = 9876543210
num = -5082
if num < 0:
    num-=num + num
mx_num = 0
mn_num = 0
while num1 > 0:
    a = num1 % 10
    if a > mx_num:
        mx_num = a
    if a < mn_num:
        mn_num = a
    num1 = num1//10
print(mx_num)
print(mn_num)
################# using functions #############

# method 1
def min_max_number(num):
    if num < 0:
        num -= num + num
    maximum_number = 0
    minimum_number = 0
    while num > 0:
        a = num % 10
        if a > maximum_number:
            maximum_number = a
        if a < minimum_number:
            minimum_number = a
        num = num//10
    return maximum_number, minimum_number
number1 = 9876543210
maximum_number1, minimum_number1 = min_max_number(number1)
print(maximum_number1,minimum_number1)

number2 = -5082
maximum_number2,minimum_number2 = min_max_number(number2)
print(maximum_number2,minimum_number2)

# method 2

def largest_smallest_digit(num):

    largest = 0
    smallest = 0
    num = str(abs(num))
    for i in num:
        if int(i) > largest:
            largest = int(i)
        if int(i) < smallest:
            smallest = int(i)
    return smallest,largest

number1 = 9876543210

smallest1, largest1 = largest_smallest_digit(number1)
print("Largest digit in 9876543210:",largest1)
print("Smallest digit in 987654321:",smallest1)

number2 = -5082

smallest2, largest2 = largest_smallest_digit(number2)
print("Largest digit in -5082:",largest2)
print("Smallest digit in -5082:",smallest2)



