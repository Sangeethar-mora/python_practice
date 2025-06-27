# Exercise: 19: Print Alternate Prime Numbers till 20
# A Prime Number is a number that can only be divided by itself and 1 without remainders (e.g., 2, 3, 5, 7, 11).
#
# For example:
#
# All prime numbers from 1 to 20: 2, 3, 5, 7, 11, 13, 17, 19
#
# Alternate prime numbers from 1 to 20:
# 2, 5, 11, 17

prime_num = []

for i in range(2, 20):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        prime_num.append(i)
for i in prime_num:
    print(i,end = " ")
print()
print("Altarnate prime numbers 1 to 20:")
for i in prime_num[::2]:
    print(i,end = " ")


