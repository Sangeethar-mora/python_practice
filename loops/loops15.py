# Exercise 15: Print elements from a given list present at odd index positions
# Given:
#
# my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# Note: The list index always starts at 0
#
# Expected output:
#
# 20 40 60 80 100

# method 1
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for i in my_list[1::2]:
    print(i,end = " ")
print()

# method 2

c = 1
for i in my_list:
    if c % 2 == 0:
        print(i,end = " ")
    c = c+1

########## using functions ########

def odd_index_positions(my_list):
    result = ""
    for i in my_list[1::2]:
        result += str(i)+" "
    return result
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(odd_index_positions(my_list))

# method 2

def odd_index_position(my_list):
    result = ""
    count = 1
    for i in my_list:
        if count % 2 == 0:
            result += str(i)+" "
        count += 1
    return result
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(odd_index_position(my_list))


