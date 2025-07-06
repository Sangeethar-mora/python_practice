# Exercise 17: Find the sum of a series of a number up to n terms
# Write a program to calculate the sum of this series up to n terms. For example, if the number is 2 and the number of terms is 5,
# then the series will be 2+22+222+2222+22222=2469
#
# Given:
#
# # number of terms
# num = 2
# terms = 5
# Expected output:
#
# 24690
num = 2
terms = 5
result = 0
for i in range(1,terms):
    num = num*10+2
    result+=num
print(result)






