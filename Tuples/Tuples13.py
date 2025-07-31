#Exercise 13: Removing Duplicates from Tuple
#Write a code to create a new tuple with only unique elements.
#
#Given:
#
#my_tuple = (1, 2, 2, 3, 4, 4, 5)
#Expected Output:
#
#Original tuple with duplicates: (1, 2, 2, 3, 4, 4, 5)
#Tuple with unique elements: (1, 2, 3, 4, 5)

my_tuple = (1, 2, 2, 3, 4, 4, 5)

tuple_unique = tuple(set(my_tuple))

print("Original tuple with duplicaates: ",my_tuple)

print("Tuple with unique elements",tuple_unique)


