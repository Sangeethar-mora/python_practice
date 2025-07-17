# Exercise 14: Remove empty strings from a list of strings
# Given:
#
# str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
# Expected Output:
#
# Original list of sting
# ['Emma', 'Jon', '', 'Kelly', None, 'Eric', '']
#
# After removing empty strings
# ['Emma', 'Jon', 'Kelly', 'Eric']

def remove_empty_string(str_list):
    new_list = []
    for i in str_list:
        if i:
            new_list.append(i)
    return new_list
str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
print("original list of string\n",str_list)
result = remove_empty_string(str_list)
print("After removing empty strings\n",result)
