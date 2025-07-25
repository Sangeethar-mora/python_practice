# Exercise 10: Display a message “Done” after the successful execution of the for loop
# For example, the following loop will execute without any error.
#
# Given:
#
# for i in range(5):
#     print(i)
# Expected output:
#
# 0
# 1
# 2
# 3
# 4
# Done!
for i in range(5):
    print(i)
else:
    print("done!")

def successful_execution():
    result = ""
    for i in range(5):
        result+=str(i)+"\n"
    result+="done!"
    return result
print(successful_execution())
