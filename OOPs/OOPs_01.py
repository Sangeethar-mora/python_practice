# OOP Exercise 1: Create a Class with instance attributes
# Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.

class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
    def display_details(self):
        print(self.max_speed, self.mileage)

car1 = Vehicle("56kms","14kmh")
car1.display_details()
