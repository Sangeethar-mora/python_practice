# Exercise 20: Print Reverse Number Pattern
# Expected Output:
#
# 1 1 1 1 1
# 2 2 2 2
# 3 3 3
# 4 4
# 5
# method 1
for i in range(1,6):
    print((str(i)+(' '))*(6-i))

# method 2
# using while loop
i = 1
while i < 6:
    print((str(i) + ' ') * (6 - i))
    i += 1
############ using functions #############

# method 1
def pattern():
    result = ""
    for num in range(1, 6):
        result+=(str(num)+(' '))*(6-num)+'\n'
    return result
print(pattern())

# method 2

def pattern(i = 1):
    result = ""
    while i < 6:
        result+= ((str(i) + ' ') * (6 - i))+'\n'
        i += 1
    return result
print(pattern())





