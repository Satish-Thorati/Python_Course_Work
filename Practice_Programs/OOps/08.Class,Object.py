#8. Temperature Converter
'''Problem: Create a class to convert Celsius to Fahrenheit and vice versa.
Answer:'''

class Temperature:
     def __init__(self, celsius):
         self.celsius = celsius
     def to_fahrenheit(self):
         return (self.celsius * 9/5) + 32
     def to_celsius(self, fahrenheit):
         return (fahrenheit - 32) * 5/9

# Example usage
temp = Temperature(25)
print("Fahrenheit:", temp.to_fahrenheit())
print("Celsius from 98F:", temp.to_celsius(98))