# Exercise 11: Percentage Display
# Ask the user for a numerator and a denominator. Calculate the percentage
# and display it with two decimal places followed by a percent sign (e.g., 75.50%).

while True:
    denominator = int(input("enter the denominator: "))
    if denominator == 0:
        print("Denimonator cannot be zero ")
    else:
        numarator = int(input("enter the numarator: "))
        result = (numarator/denominator)
        percentage = result*100
        print("%.2f" % percentage,"%")
        break

################# using definations ##################

def percentage_display(Denominator, Numarator):
    if Denominator == 0:
        return "Denominator can not be zero"
    else:
        result = (Numarator/Denominator)
        percentage = result * 100
        return "%0.2f" % percentage + " %"
Denominator = int(input("enter the denominator: "))
Numarator = int(input("enter the numarator: "))
print(percentage_display(Denominator, Numarator))

