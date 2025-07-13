# Exercise 6: Write all content of a file into a new file by skipping line number 5
# Create a test.txt file and add the below content to it.
#
# Given test.txt file:
#
# line1
# line2
# line3
# line4
# line5
# line6
# line7
# Expected Output: new_file.txt
#
# line1
# line2
# line3
# line4
# line6
# line7

with open("test.txt", "w") as file:
    file.write("line1\nline2\nline3\nline4\nline5\nline6\nline7")

with open("test.txt","r") as file:
    content = file.readlines()

with open("new_test.txt","w") as file:
    c = 1
    for i in content:
        if c != 5:
            file.write(i)
        c += 1

with open("new_test.txt", "r") as file:
    content = file.read()
    print(content)

############ using functions ###############

def skipping_line5():
    with open("test.txt", "w") as file:
        file.write("line1\nline2\nline3\nline4\nline5\nline6\nline7")

    with open("test.txt","r") as file:
        content = file.readlines()

    with open("new_test.txt","w") as file:
        c = 1
        for i in content:
            if c != 5:
                file.write(i)
            c += 1

    with open("new_test.txt", "r") as file:
        content = file.read()
    return content

print(skipping_line5())



