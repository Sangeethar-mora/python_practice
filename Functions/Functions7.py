# Exercise 7: Assign a different name to function and call it through the new name
# Below is the function display_student(name, age). Assign a new name show_student(name, age) to it and call it using the new name.
#
# Given:
#
# def display_student(name, age):
#     print(name, age)
#
# display_student("Emma", 26)
# You should be able to call the same function using
#
# show_student(name, age)

def display_student(name, age):
    print(name, age)

display_student("emma", 26)
show_student = display_student
show_student("berry", 20)
