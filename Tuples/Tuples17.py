# Exercise 17: Sort a tuple of tuples by 2nd item
# Given:
#
# tuple1 = (('a', 23),('b', 37),('c', 11), ('d',29))
# Expected output:
#
# (Sorted tuple by 2nd item: (('c', 11), ('a', 23), ('d', 29), ('b', 37))

tuple1 = (('a', 23),('b', 37),('c', 11), ('d',29))

num_list = ( i[1] for i in tuple1)
sorted_list = sorted(num_list)
tuple2 = []
for i in sorted_list:
    for j in tuple1:
        if i == j[1]:
            tuple2.append(j)
print(f"Sorted tuple by 2nd item: {tuple(tuple2)}")

