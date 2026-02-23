#25. Vehicle Sounds

class Vehicle:
     def sound(self):
         pass

class Truck(Vehicle):
    def sound(self):
         print("Honk Honk!")

class Train(Vehicle):
    def sound(self):
        print("Choo Choo!")

for v in [Truck(), Train()]:

   v.sound()