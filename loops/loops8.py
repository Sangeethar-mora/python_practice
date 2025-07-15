# Exercise 8: Print list in reverse order using a loop
# Given:
#
# list1 = [10, 20, 30, 40, 50]
# Expected output:
#
# 50
# 40
# 30
# 20
# 10
list1 = [10, 20, 30, 40, 50]
for i in list1[::-1]:
    print(i)

############# using functions ########

def reverse_list(user_list):
    result = ""
    for i in list1[::-1]:
        result += f"{i}\n"
    return result
sorted_list = reverse_list([10, 20, 30, 40, 50])
print(sorted_list)

