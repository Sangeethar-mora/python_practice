# Exercise 19: Print Full Multiplication Table
# The multiplication table from 1 to 10 is a table that shows the products of numbers from 1 to 10.
#
# Write a code to generates a complete multiplication table for numbers 1 through 10.
#
# Given:
#
# multiplication table of: 1
#  1 2 3 4 5 6 7 8 9 10
# multiplication table of: 2
#  2 4 6 8 10 12 14 16 18 20
# multiplication table of: 3
#  3 6 9 12 15 18 21 24 27 30
# ...
# multiplication table of: 10
#  10 20 30 40 50 60 70 80 90 100

for i in range(1,11):
    print(f"multiplication table of: {i}")
    for j in range(1,11):
        print(i*j,end = " ")
    print()

############# using functions #############
def multiplication_table():
    result = ""
    for i in range(1,11):
        result += f"multiplication table of: {i}"+"\n"
        for j in range(1,11):
            result += (str(i * j)+" ")
        result += "\n"
    return result
print(multiplication_table())
