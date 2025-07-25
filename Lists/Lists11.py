# Exercise 11: Remove empty strings from the list of strings
# list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
# Expected output:
#
# ["Mike", "Emma", "Kelly", "Brad"]

def remove_empty_string(list1):
    res = list(filter(None, list1))
    return res
list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
print(remove_empty_string(list1))
