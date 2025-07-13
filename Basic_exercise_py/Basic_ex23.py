# Exercise 23: Create a simple countdown timer using a while loop.
# Write a code to create a simple countdown timer of 5 seconds using a while loop.
#
# Once the timer finishes (when the remaining time reaches zero), print a “Time’s up!” message.
#
# Expected Output:
#
# Time remaining: 5 seconds
# Time remaining: 4 seconds
# Time remaining: 3 seconds
# Time remaining: 2 seconds
# Time remaining: 1 seconds
# Time's up!
n = 5
while n > 0:
    print(f"time remainig: {n} seconds")
    n = n-1
print("time's up !")

################# using functions ############

def countdown_timer(n = 5):
    result = ""
    while n > 0:
        result += f"time remainig: {n} seconds"+"\n"
        n = n-1
    result+="time's up !"
    return result
print(countdown_timer())
