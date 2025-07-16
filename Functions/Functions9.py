# Exercise 9: Find the largest item from list
# Given:
#
# x = [4, 6, 8, 24, 12, 2]
# Expected Output:
#
# 24

def largest_item(x):
    largest = 0
    for i in x:
        if i > largest:
            largest = i
    return largest
x = [4, 6, 8, 24, 12, 2]
print(largest_item(x))
