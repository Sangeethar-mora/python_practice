# Exercise 1: Print first 10 natural numbers using while loop
# Expected output:
#
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# n = 1
# while n <= 10:
#     print(n)
#     n = n+1

############### using functions ##########

def ten_natural_numbers():
    n = 1
    result = ""
    while n <= 10:
        result += str(n) + "\n"
        n = n + 1
    return result
print(ten_natural_numbers())

