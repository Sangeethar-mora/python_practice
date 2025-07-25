# Exercise 12: Display Fibonacci series up to 10 terms
# Have you ever wondered about the Fibonacci Sequence? It’s a series of numbers in which the next number is found by adding up the two numbers before it. The first two numbers are 0 and 1.
#
# For example, 0, 1, 1, 2, 3, 5, 8, 13, 21. The next number in this series is 13 + 21 = 34.
#
# Expected output:
#
# Fibonacci sequence:
# 0  1  1  2  3  5  8  13  21  34

cur = 0
pev = 1
print("Display Fibonacci series up to 10 terms")
for i in range(10):
    print(cur,end = "  ")
    res = cur + pev
    pev = cur
    cur = res
# this print used just to print function method output in new line
print()
def fibonacci_series():
    cur = 0
    pev = 1
    result = ""
    for i in range(10):
        result+=str(cur)+"  "
        res = cur + pev
        pev = cur
        cur = res
    return result

print("Display Fibonacci series up to 10 terms")
print(fibonacci_series())
