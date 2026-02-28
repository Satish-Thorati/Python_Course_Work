#36. Abstract Payment Method

from abc import ABC, abstractmethod

class Payment(ABC):
   @abstractmethod

   def pay(self, amount):
      pass

class UPI(Payment):
    def pay(self, amount):
          print(f"Paid {amount} via UPI")

p = UPI()
p.pay(300)