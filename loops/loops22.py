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
num2 = -5082
num = -5082

if num < 0:
    num-=num + num
    print(num)
mx_num = 0
mn_num = 0
while num1 > 0:
    a = num1%10
    if a > mx_num:
        mx_num = a
    if a < mn_num:
        mn_num = a
    num1 = num1//10


print(mx_num)
print(mn_num)




