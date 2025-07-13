# Check Palindrome Number
# A palindrome number is a number that remains the same when its digits are reversed. In simpler terms, it reads the same forwards and backward. For example 121, 5005.
#
# Write a code to check if given number is palindrome.
number = int(input("enter the number"))
n = number
rev = 0
while n>0:
    rem=n%10
    rev= (rev*10)+rem
    n=n//10

print(rev)
if(number == rev):
    print(True)
else:
    print(False)
############### using functions ############

def palindrom(number):
    revision = 0
    given_number = number
    while number > 0:
        reminder = number % 10
        revision = (revision * 10 ) + reminder
        number = number // 10
    if given_number == revision:
        return 'True'
    else:
        return 'False'
print(palindrom(121))


