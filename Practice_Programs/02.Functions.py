#11. Sort a List
elements = list(map(int, input("Enter list elements: ").split()))
elements.sort()
print("Sorted list:", elements)

#12. Clear a List Inside Function
def clear_list(lst):
    lst.clear()

elements = list(map(int, input("Enter list elements: ").split()))
clear_list(elements)
print("Cleared list:", elements)

#13. Update Dictionary Value
data = eval(input("Enter dictionary: "))
key = input("Enter key to update: ")
value = int(input("Enter new value: "))

data[key] = value
print("Updated dictionary:", data)

#14. Remove Element from List by Value
elements = list(map(int, input("Enter list elements: ").split()))
remove_item = int(input("Enter element to remove: "))

if remove_item in elements:
    elements.remove(remove_item)

print("Updated list:", elements)

#15. Add Key to Dictionary
data = eval(input("Enter dictionary: "))
key = input("Enter new key: ")
value = int(input("Enter new value: "))

data[key] = value
print("Updated dictionary:", data)

#16. Increment All Values in Dictionary
data = eval(input("Enter dictionary: "))

for key in data:
    data[key] += 1

print("Updated dictionary:", data)

#17. Factorial of a Number
num = int(input("Enter a number: "))
fact = 1

for i in range(1, num + 1):
    fact *= i

print("Factorial is:", fact)

#18. Fibonacci Number (Nth Term)
n = int(input("Enter term number: "))

a, b = 0, 1
for _ in range(n - 1):
    a, b = b, a + b

print("Fibonacci number is:", a)

#19. Sum of First N Natural Numbers
n = int(input("Enter a number: "))
total = n * (n + 1) // 2
print("Sum is:", total)

#20. Reverse a String Using Recursion
def reverse_string(s):
    if len(s) == 0:
        return s
    return reverse_string(s[1:]) + s[0]

text = input("Enter a string: ")
print("Reversed string is:", reverse_string(text))