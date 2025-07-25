# Exercise 15: Access Nested Lists
# Given a nested list, print the element '55'.

def Access_Nested_lists(nested_list):

    return f"Given a nested list, printed the element:   {nested_list[1][1]}"

nested_list = [[10, 20, 30], [44, 55, 66], [77, 87, 99]]
print(Access_Nested_lists(nested_list))
