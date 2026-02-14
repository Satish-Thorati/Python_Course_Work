#9. Inventory Management
'''Problem: Create an item that tracks and updates quantity.
Answer:'''

class InventoryItem:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity
    def update_quantity(self, amount):
        self.quantity += amount
    def display(self):
        print(f"{self.name}: {self.quantity} in stock")

# Object usage
item = InventoryItem("Mouse", 50)
item.update_quantity(-5)
item.display()