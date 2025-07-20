# Exercise 10: remove duplicates from a list
# Write a code to remove duplicates from a list and create a tuple and find the minimum and maximum number
#
# Given:
#
# sample_list = [87, 45, 41, 65, 94, 41, 99, 94]
# Expected Outcome:
#
# unique items [87, 45, 41, 65, 99]
# tuple (87, 45, 41, 65, 99)
# min: 41
# max: 99

def remove_duplicates_from_a_list(sample_list):
    unique_items = list(set(sample_list))

    return f"unique items {unique_items}\ntuple {tuple(unique_items)}\nmin: {min(unique_items)}\nnmax: {max(unique_items)}"
sample_list = [87, 45, 41, 65, 94, 41, 99, 94]
print(remove_duplicates_from_a_list(sample_list))
