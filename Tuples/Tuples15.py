#Exercise 15: Map Tuples
#Given a tuple of numbers, create a new tuple where each number is squared.
#
#Given:
#
#t = (1, 2, 3, 4)
#Expected Output:
#
#Original tuple: (1, 2, 3, 4)
#Squared tuple:  (1, 4, 9, 16)

my_tuple = (1, 2, 3, 4)

squared_tiple = []

for i in my_tuple:
    squared_tiple.append(i**2)

print("Squared tuple: ",tuple(squared_tiple))






