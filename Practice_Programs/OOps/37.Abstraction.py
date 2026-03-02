#37. Abstract Vehicle

from abc import ABC, abstractmethod

class Vehicle(ABC):
  @abstractmethod
  def move(self):
    pass

class Scooter(Vehicle):
   def move(self):
       print("Scooter is moving")

s = Scooter()
s.move()