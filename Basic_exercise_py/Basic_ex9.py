# Exercise 9: Check Palindrome Number
# Write a Python code to check if the given number is a palindrome. A palindrome number reads the same forwards and backward. For example, 545 is a palindrome number.
#
# Expected Output:
#
# original number 121
# Yes. given number is palindrome number
#
# original number 125
# No. given number is not palindrome number

# original number 1231
n = 1231
number=n
rev=0
while n>0:
    rem=n%10 #1 3 2 1
    rev= (rev*10)+rem #1 13 132 1321
    n=n//10 #123 12 1 0

print(rev)
if(n==rev):
    print(True)
else:
    print(False)

############# using functions ##################

def palindrom_number(number):
    rev = 0
    while number > 0:
        rem = number % 10
        rev = (rev * 10) + rem
        number = number // 10
    if number == rev:
        return True
    else:
        return False
print(palindrom_number(1231))
