# Exercise 14: Tabular Output from Lists
# You have two lists: names = ["Alice", "Bob", "Charlie"] and scores = [85, 92, 78]. Print these lists as a simple table with columns “Name” and “Score”.
#
# Expected Output:
#
# Name       Score
# ---------------
# Alice      85
# Bob        92
# Charlie    78

names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

print(f"{"Name":<10} Scores")
print("-"*17)
for i in range(3):
    print(f"{names[i]:<12}{scores[i]}")

############# using functions ############

def tabular_output(names, scores):
    result = ""
    result += f"{"Name":<10} Scores"+"\n"
    result += "-"*17+"\n"
    for i in range(3):
        result+=f"{names[i]:<12}{scores[i]}"+"\n"
    return result
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]
print(tabular_output(names, scores))

