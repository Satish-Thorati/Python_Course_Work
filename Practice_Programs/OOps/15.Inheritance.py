#15. Shape and Rectangle

class Shape:
    def __init__(self, color):
        self.color = color
    def display_color(self):
        print(f"Color: {self.color}")

class Rectangle(Shape):
    def __init__(self, color, length, width):
        super().__init__(color)
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

rect = Rectangle("Blue", 4, 5)
rect.display_color()
print("Area:", rect.area())