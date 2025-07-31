# Exercise 6: Count Character Frequencies
# Given a string, create a dictionary where keys are characters and values are their frequencies in the string.
#
# Given:
#
# string1 = 'Jessa'
# Expected Output:
#
# Frequencies for 'Jessa': {'J': 1, 'e': 1, 's': 2, 'a': 1}
string1 = 'Jessa'
count_str = []
for i in string1:
    count_str.append(i)
counts = {}
for item in count_str:
    if item in counts:
        counts[item] += 1
    else:
        counts[item] = 1
print(counts)

