# Print a downward half-pyramid pattern of stars
# * * * * *
# * * * *
# * * *
# * *
# *

for i in range(5, 0, -1):
    print("* " *i)
################### using while loop ###

n = 5
while n > 0:
    print("* " *n)
    n = n-1
######## using functions()#########

def pattern(n = 5):
    while n > 0:
        print("* "*n)
        n = n - 1
pattern()
