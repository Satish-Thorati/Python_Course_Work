#24. Shape Areas

class Shape:
   def area(self):
      pass

class Circle(Shape):
   def area(self):
       return 3.14 * 7 * 7

class Square(Shape):
   def area(self):
       return 5 * 5


s1 = Circle()
s2 = Square()
print(s1.area())
print(s2.area())