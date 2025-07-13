# Exercise 3: Display Decimal Number to Octal using print() function
# oct() gives oct number and oct number eg oct(8) as 0o10

num = int(input("enter number: "))
print(oct(num))
print("%o" % num)
print("%o" % 8)

########## using functions ###########

def octal_number(number):
    result = oct(number)
    result1 =" %o" % number
    return result, result1
number = int(input("enter number: "))
print(octal_number(number))
