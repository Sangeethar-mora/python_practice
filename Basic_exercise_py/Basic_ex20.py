# Exercise 20: Print Reverse Number Pattern
# Expected Output:
#
# 1 1 1 1 1
# 2 2 2 2
# 3 3 3
# 4 4
# 5

for i in range(1,6):
    print((str(i)+(' '))*(6-i))

################ using while loop ##########

i = 1
while i < 6:
    print((str(i) + ' ') * (6 - i))
    i += 1

