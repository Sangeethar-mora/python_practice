# Exercise 4: Count the occurrence of each element from a list
# Write a program to iterate a given list and count the occurrence of each element and create a dictionary to show the count of each element.
#
# Given:
#
# sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
# Expected Output:
#
# Printing count of each item   {11: 2, 45: 3, 8: 1, 23: 2, 89: 1}

def count_the_occurrence(sample_list):

    count_list = {}
    for num in sample_list:
        if num in count_list:
            count_list[num] += 1
        else:
            count_list[num] = 1
    return f"Printing count of each item   {count_list}"

sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
print(count_the_occurrence(sample_list))
