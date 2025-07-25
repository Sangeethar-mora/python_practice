# Exercise 3: Sum and average of all numbers in a list
# Calculate and print the sum and average of all numbers in a list.
#
# Given:
#
# my_list = [10, 20, 30, 40, 50]
# Expected Output:
#
# Sum: 150
# Average: 30.0

def sum_avg(my_list):
    return f"sum : {sum(my_list)}\n Average: {sum(my_list)/len(my_list)}"
my_list = [10, 20, 30, 40, 50]
print(sum_avg(my_list))
