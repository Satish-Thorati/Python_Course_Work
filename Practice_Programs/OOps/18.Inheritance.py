#18. Vehicle and Bike

class Vehicle:
    def drive(self):
        print("Driving a vehicle")

class Bike(Vehicle):

    def wheel_count(self):
        print("2 wheels")

b = Bike()
b.drive()
b.wheel_count()