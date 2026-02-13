#7. Product Discount System
'''Problem: Create Product class with discount application logic.
Answer:'''


class Product:
     def __init__(self, name, price):
         self.name = name
         self.price = price
     def apply_discount(self, percent):
         self.price -= self.price * (percent / 100)
     def show_price(self):
         print(f"Discounted price: {self.price}")

# Create and apply
p = Product("Laptop", 50000)
p.apply_discount(10)
p.show_price()