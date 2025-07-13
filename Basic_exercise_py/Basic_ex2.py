
# Exercise 2: Print the Sum of a Current Number and a Previous number
# Write a Python code to iterate the first 10 numbers, and in each iteration, print the sum of the current and previous number.

print("Current Number 0 Previous Number 0  Sum: 0")
for i in range(11):
    pn = i-1
    sm = (i+(i-1))

    # if pn < 0:
    #  pn, sm = 0,0
    # sm = 0
    if pn<0:
        pn = 0
    if sm < 0:
        sm = 0
    #
    print("current number", i, "previous number", pn, "sum:", sm)
################# using functions #######

def current_prev_sum():
    print("Current Number 0 Previous Number 0 Sum:  0")
    for i in range(1, 10):
        Previous = i-1
        sum_of_all = i+(i-1)
        print('Current Number', i, 'Previous Number', Previous, 'Sum: ', sum_of_all)
current_prev_sum()




