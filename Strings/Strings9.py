# Exercise 9: Calculate the sum and average of the digits present in a string
# Given a string s1, write a program to return the sum and average of the digits that appear in the string, ignoring all other characters.
#
# Given:
#
# str1 = "PYnative29@#8496"
# Expected Outcome:
#
# Sum is: 38 Average is  6.333333333333333

def cal_sum_average(str1):
    total = 0
    count = 0
    for i in str1:
        if i.isdigit():
            total+=int(i)
            count+=1
    average = total/count
    return f"Sum is: {total} Average is {average}"

str1 = "PYnative29@#8496"
result = cal_sum_average(str1)
print(result)

