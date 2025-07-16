# Exercise 12: Modifies global variable
# Define a global variable global_var = 10.
# Write a function that modifies a global variable value.
global_var = 10
def modifies_global_variable():
    global_var = 30
    print("inside function",global_var)
modifies_global_variable()
print("outside function",global_var)


