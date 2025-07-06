# Exercise 15: Print elements from a given list present at odd index positions
# Given:
#
# my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# Note: The list index always starts at 0
#
# Expected output:
#
# 20 40 60 80 100
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for i in my_list[1::2]:
    print(i,end = " ")
print()

###############################3
c = 1
for i in my_list:
    if c % 2 == 0:
        print(i,end = " ")
    c = c+1



