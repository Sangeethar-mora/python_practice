# Exercise 18: Concatenate two lists in the following order
# list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]
# Expected output:
#
# ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']

def concatenate_list(list1, list2):
    new_list_concatenate = []
    for i in range(0, len(list1)):
        for j in range(0, len(list2)):
            new_list_concatenate.append(list1[i]+list2[j])
    return new_list_concatenate
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
print(concatenate_list(list1, list2))
