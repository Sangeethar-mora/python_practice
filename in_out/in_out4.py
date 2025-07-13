# Exercise 4: Display Float Number with 2 Decimal Places
# Given:
#
# num = 458.541315
# Expected Output:
#
# 458.54
# "%0.2f" we can change the number according to the decimal places we need eg : %0.4f


number = 458.541315
print(str(number)[:6])
print("%0.2f" % number)

################# using functions ###########

def number_two_decimal(number):
    return "%0.2f" % number
print(number_two_decimal(458.541315))


