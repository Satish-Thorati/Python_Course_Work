#35. Encapsulation in Product

class Product:
   def __init__(self):
        self.__stock = 100
   def buy(self, quantity):
       if quantity <= self.__stock:
           self.__stock -= quantity
       else:
           print("Out of stock")

   def check_stock(self):
        return self.__stock

p = Product()
p.buy(20)
print(p.check_stock())