# Exercise 5: Check if the first and last numbers of a list are the same
# Write a code to return True if the list’s first and last numbers are the same. If the numbers are different, return False.
#
# Given:
#
# numbers_x = [10, 20, 30, 40, 10]
# # output True
#
# numbers_y = [75, 65, 35, 75, 30]
# # Output False


numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]

first = numbers_x[0]
last = numbers_x[-1]

if first == last:
    print("true",numbers_x)
else:
    print("false",numbers_x)

first = numbers_y[0]
last = numbers_y[-1]
if first == last:
    print("true",numbers_y)
else:
    print("false",numbers_y)

#########################################3
numbers_x = [10, 20, 30, 40, 10]
c = 0
x = []

for i in numbers_x:
    if (c == 0) or c == (len(numbers_x)-1):
        x.append(i)
    c+=1
print(x)
