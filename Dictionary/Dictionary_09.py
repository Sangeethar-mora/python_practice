# Exercise 9: Modify Nested Dictionary
# In the below dictionary, change name to ‘Jessa’.
#
# Given:

nested_student_dict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}

nested_student_dict["class"]["student"]["name"] = "jessa"

print(nested_student_dict)
