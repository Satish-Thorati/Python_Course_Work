#1. Add Two Numbers
a, b = map(int, input("Enter two numbers: ").split())
print("The sum is:", a + b)

#2. Square a Number
n = int(input("Enter a number: "))
print("The square is:", n * n)

#3. Area of a Circle
r = float(input("Enter radius: "))
area = 3.14 * r * r
print("Area of circle is:", round(area, 2))

#4. Greet the User
name = input("Enter your name: ")
print("Hello,", name)

#5. Convert Celsius to Fahrenheit
c = float(input("Enter temperature in Celsius: "))
f = (c * 9/5) + 32
print("Temperature in Fahrenheit:", f)

#6. Multiply Three Numbers
a, b, c = map(int, input("Enter three numbers: ").split())
print("Product is:", a * b * c)

#7. Calculate Simple Interest
p, r, t = map(float, input("Enter Principal, Rate, and Time: ").split())
si = (p * r * t) / 100
print("Simple Interest is:", si)

#8. Find Length of a String
s = input("Enter a string: ")
print("Length of string is:", len(s))

#9. Append to a List
lst = list(map(int, input("Enter list elements separated by space: ").split()))
x = int(input("Enter element to append: "))
lst.append(x)
print("Updated list:", lst)

#10. Double Each Element in a List
lst = list(map(int, input("Enter list elements: ").split()))
doubled = [x * 2 for x in lst]
print("Doubled list:", doubled)