# Exercise 14: Reverse a integer number
# Given:
#
# 76542
#
# Expected output:
#
# 24567

n = 76542
rev = 0
while n > 0:
    rem = n % 10
    rev = (rev * 10) + rem
    n = n//10
print(rev)

############ using function #########

def reverse_int_string(number = 76542):
    reverse = 0
    while number > 0:
        reminder = number % 10
        reverse = (reverse * 10) + reminder
        number = number // 10
    return reverse
print(reverse_int_string())
