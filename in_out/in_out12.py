# Exercise 12: Interactive Menu
# Create a simple interactive menu with options like “1. Say Hello”, “2. Calculate Square”, “3. Exit”.
# Based on the user’s input, perform the corresponding action

while True:
    print("Menu")
    print("1.Hello Buddy")
    print("2.Calculate Square")
    print("3.exit")
    option_choose = int(input("enter any option from 1 to 3 "))

    if option_choose == 1:
        print("Hello Buddy")
    elif option_choose == 2:
        no = int(input("enter the number to square: "))
        square = int(no) ** 2
        print(f"the {no} of square is ", square)
    elif option_choose == 3:
        print("Exit")
        break
    else:
        print("please select the options from 1 to 3 only")

############## using functions ########################

def Interactive_menu():
    while True:
        option_choose = int(input("enter any option from 1 to 3 "))
        if option_choose == 1:
            return "Hello Buddy"
        elif option_choose == 2:
            no = int(input("enter the number to square: "))
            square = int(no) ** 2
            return f"the {no} of square is ", square
        elif option_choose == 3:
            return "Exit"
        else:
            return "please select the options from 1 to 3 only"
print("Menu")
print("1.Hello Buddy")
print("2.Calculate Square")
print("3.exit")
print(Interactive_menu())
