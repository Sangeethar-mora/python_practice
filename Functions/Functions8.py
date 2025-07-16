# Exercise 8: Generate a Python list of all the even numbers between 4 to 30
# Expected Output:
#
# [4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]

def even_numbers():
    result = []
    for i in range(4, 31):
        if i % 2 == 0:
            result.append(i)
    return result
print(even_numbers())
