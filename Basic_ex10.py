# Exercise 10: Merge two lists using the following condition
# Given two lists of numbers, write Python code to create a new list containing odd numbers from the first list and even numbers from the second list.
#
# Given:
#
# list1 = [10, 20, 25, 30, 35]
# list2 = [40, 45, 60, 75, 90]
# Expected Output:
#
# result list: [25, 35, 40, 60, 90]


list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

result = []

for i in list1:
    if i%2 != 0:
        # print(list[i])
        result.append(i)

for i in list2:
    if i%2 == 0:
        # print(list[i])
        result.append(i)
print(result)
