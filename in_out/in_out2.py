# Format Output String
# Write a program to display four string “My, “Name“, “Is“, “James” as “My**Name**Is**James“.
#
# Use the print() function to format the given words in the specified format.
# Display the ** separator between each string.

str1 = 'My'
str2 = 'Name'
str3 = 'Is'
str4 = 'James'
print(str1, str2, str3, str4, sep = "**")

############ using functions ############

def format_output_string(*char):
    result = ""
    for i in range(len(char)):
        result += char[i]
        if i != len(char)-1:
            result += "**"
    return result
str1 = 'My'
str2 = 'Name'
str3 = 'Is'
str4 = 'James'
print(format_output_string(str1, str2, str3, str4))
