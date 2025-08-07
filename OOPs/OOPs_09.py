# OOP Exercise 9: Check object is a subclass of a particular class
# Given:
#
# class Animal:
#     pass
#
# class Dog(Animal):
#     pass
#
# class Puppy(Dog):
#     pass
#
# class Cat:
#     pass
# Write a code to check the following
#
# Dog is a subclass of Animal? –> True
# Animal is a subclass of Dog? –> False
# Cat is a subclass of Animal? –> False
# Puppy is a subclass of Animal –> True

class Animal:
    pass

class Dog(Animal):
    pass

class Puppy(Dog):
    pass

class Cat:
    pass

print("Dog is a subclass of Animal? –> ",format(issubclass(Dog, Animal)))
print("Animal is a subclass of Dog? –> ",issubclass(Animal, Dog))
print("Cat is a subclass of Animal? –> ",issubclass(Cat, Animal))
print("Puppy is a subclass of Animal –> ",issubclass(Puppy, Animal))

