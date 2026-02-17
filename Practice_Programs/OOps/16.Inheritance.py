#16. Appliance and WashingMachine

class Appliance:
    def __init__(self, brand):
        self.brand = brand

class WashingMachine(Appliance):
    def wash(self):
        print(f"{self.brand} washing clothes.")

wm = WashingMachine("LG")
wm.wash()