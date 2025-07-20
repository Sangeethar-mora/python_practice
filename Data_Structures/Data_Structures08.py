# Exercise 8: Filter List Against Dictionary Values
# Write a program to iterate a given list and check if a given element exists as a key’s value in a dictionary. If not, delete it from the list
#
# Given:
#
# roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
# sample_dict = {'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}
# Expected Outcome:
#
# After removing unwanted elements from list [47, 69, 76, 97]

def filter_list(roll_number, sample_dect):
    unwanted_list = []
    for i in roll_number:
        if i in sample_dect.values():
            unwanted_list.append(i)
    return f"After removing unwanted elements from list  {unwanted_list}"
roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
sample_dict = {'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}
print(filter_list(roll_number, sample_dict))
