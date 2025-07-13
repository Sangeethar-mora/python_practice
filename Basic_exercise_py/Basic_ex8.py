# Exercise 8: Print the following pattern
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

############# using nested for loop ################
for i in range(1, 6):
    for j in range(i):
        print(i, end=" ")
    print()
############## using for loop #################
for i in range(1, 6):
    print((str(i)+" ")*i)

############## using while loop #################
n = 1
while n < 6:
    print((str(n)+" ")*n)
    n = n+1

#################### using functions #############

def pattern():
    for i in range(1, 6):
        for j in range(i):
            print(i, end=" ")
        print()
pattern()

def pattern():
    for i in range(1, 6):
        print((str(i)+" ")*i)
pattern()
