# Check Palindrome Number
# A palindrome number is a number that remains the same when its digits are reversed. In simpler terms, it reads the same forwards and backward. For example 121, 5005.
#
# Write a code to check if given number is palindrome.
number = int(input("enter the number"))
n = number
rev = 0
rev=0
while n>0:
    rem=n%10
    rev= (rev*10)+rem
    n=n//10

print(rev)
if(number == rev):
    print(True)
else:
    print(False)



