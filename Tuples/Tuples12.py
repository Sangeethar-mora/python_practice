# Exercise 12: Comparing Tuples
# Compare two tuples and find out which one is “greater” and why?
#
# Given:
#
# t1 = (1, 2, 3)
# t2 = (1, 2, 4)
# Expected Output:
#
# Tuple 1: (1, 2, 3, 8)
# Tuple 2: (1, 2, 4, 5)
# (1, 2, 3, 8) is less than (1, 2, 4, 5)

t1 = (1, 2, 3)
t2 = (1, 2, 4)

if t1 > t2:
    print(f"{t1} is greater than {t2} ")
elif t1 < t2:
    print(f"{t1} is less than {t2}")
else:
    print(f"{t1} is equall to {t2}")

