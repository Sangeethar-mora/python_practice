# Exercise 19: Sort Dictionary by Values
# Sort a dictionary by its values and print the sorted dictionary (as an OrderedDict or by converting to a list of tuples).
#
# Given:
#
# my_dict = {'Jessa': 3, 'Kelly': 1, 'Jon': 2, 'Kerry': 4, 'Joy': 1}
# Expected Output:
#
# Original dictionary: {'Jessa': 3, 'Kelly': 1, 'Jon': 2, 'Kerry': 4, 'Joy': 1}
#
# Sorted by values (as OrderedDict):
# OrderedDict([('Jessa', 3), ('Kelly', 1), ('Jon', 2), ('Kerry', 4), ('Joy', 1)])

my_dict = {'Jessa': 3, 'Kelly': 1, 'Jon': 2, 'Kerry': 4, 'Joy': 1}

dict_val = my_dict.values()
sort_dict = sorted(dict_val)
ordereddict = []
for i in sort_dict:
    for k, j in my_dict.items():
        if i == j:
            ordereddict.append((k,j))
            my_dict.pop((k))
            break

print("Sorted by values (as OrderedDict):",(ordereddict))



