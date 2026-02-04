#21. Power of a Number (a^b using recursion)
def power(a, b):
    if b == 0:
        return 1
    return a * power(a, b - 1)

a, b = map(int, input("Enter base and exponent: ").split())
print("Result is:", power(a, b))

#22. Sum of Digits Using Recursion
def sum_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_digits(n // 10)

num = int(input("Enter a number: "))
print("Sum of digits:", sum_digits(num))

#23. Check Palindrome String Using Recursion
def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

text = input("Enter a string: ")
print("Is palindrome:", is_palindrome(text))

#24. GCD of Two Numbers Using Recursion
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

a, b = map(int, input("Enter two numbers: ").split())
print("GCD is:", gcd(a, b))

#25. Maximum of Three Numbers Using max()
a, b, c = map(int, input("Enter three numbers: ").split())
print("Maximum is:", max(a, b, c))

#26. Sort a List Using sorted()
elements = list(map(int, input("Enter list elements: ").split()))
print("Sorted list:", sorted(elements))

#27. Sum of Elements Using sum()
elements = list(map(int, input("Enter list elements: ").split()))
print("Sum of list is:", sum(elements))

#28. Find Data Type Using type()
value = eval(input("Enter any value: "))
print("Data type is:", type(value))

#29. Print Even Numbers up to N
n = int(input("Enter a number: "))
print("Even numbers:", end=" ")

for i in range(0, n + 1, 2):
    print(i, end=" ")

#30. Return List of Squares
elements = list(map(int, input("Enter list elements: ").split()))
squares = [x ** 2 for x in elements]
print("Squared list:", squares)