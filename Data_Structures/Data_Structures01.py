# Exercise 1: List Creation using two lists
# Write a code to create a new list using odd-indexed elements from the first list and even-indexed elements from the second
#
# Given two lists, l1 and l2, write a program to create a third list l3 by picking an odd-index element from the list l1 and even index elements from the list l2.
#
# Given:
#
# l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]
# Expected Output:
#
# Element at odd-index positions from list one
# [6, 12, 18]
# Element at even-index positions from list two
# [4, 12, 20, 28]
#
# Printing Final third list
# [6, 12, 18, 4, 12, 20, 28]

def odd_even_index_position(l1, l2):
    odd_index = []
    even_index = []
    final = []
    for num in l1:
        if num % 2 == 0:
            odd_index.append(num)
            final.append(num)
    even_index = []
    c = 1
    for num in l2:
        if c % 2 != 0:
            even_index.append(num)
            final.append(num)
        c += 1
    return f"Element at odd-index positions from list one\n{odd_index}\nElement at even-index positions from list two\n{even_index}\nPrinting Final third list\n{final}"
l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]
print(odd_even_index_position(l1, l2))

