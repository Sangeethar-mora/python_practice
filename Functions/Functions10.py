# Exercise 10: Call Function using both positional and keyword arguments
# Define a function describe_pet(animal_type, pet_name)

def describe_pet(animal_type, pet_name):
    return f"I have a {animal_type} named {pet_name}."

print(describe_pet("dog", "lucchi"))
print(describe_pet("cat", "luci"))

result1 = describe_pet(animal_type = "fish", pet_name= "winny")
result2 = describe_pet(pet_name="rem", animal_type = "horse" )
print(result1)
print(result2)

