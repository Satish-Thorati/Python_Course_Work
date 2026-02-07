"""
========================================
RECURSION QUESTIONS – PYTHON (ONE SHEET)
========================================
"""

# --------------------------------------------------
# 1. Print numbers from 1 to N
# Question:
# Write a recursive function that prints numbers from 1 to N in increasing order.
#
# Test Cases:
# Input: 5 → Output: 1 2 3 4 5
# Input: 3 → Output: 1 2 3
# --------------------------------------------------

def print_1_to_n(n):
    if n == 0:
        return
    print_1_to_n(n - 1)
    print(n, end=" ")

print_1_to_n(5)
print()
print_1_to_n(3)
print("\n")


# --------------------------------------------------
# 2. Print numbers from N to 1
# Question:
# Write a recursive function that prints numbers from N to 1 in decreasing order.
#
# Test Cases:
# Input: 4 → Output: 4 3 2 1
# Input: 2 → Output: 2 1
# --------------------------------------------------

def print_n_to_1(n):
    if n == 0:
        return
    print(n, end=" ")
    print_n_to_1(n - 1)

print_n_to_1(4)
print()
print_n_to_1(2)
print("\n")


# --------------------------------------------------
# 3. Sum of first N natural numbers
# Question:
# Write a recursive function to calculate the sum of first N natural numbers.
#
# Test Cases:
# Input: 4 → Output: 10
# Input: 6 → Output: 21
# --------------------------------------------------

def sum_n(n):
    if n == 0:
        return 0
    return n + sum_n(n - 1)

print(sum_n(4))
print(sum_n(6))
print()


# --------------------------------------------------
# 4. Factorial of a number
# Question:
# Write a recursive function to find the factorial of a number.
#
# Test Cases:
# Input: 5 → Output: 120
# Input: 3 → Output: 6
# --------------------------------------------------

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))
print(factorial(3))
print()


# --------------------------------------------------
# 5. Reverse a string using recursion
# Question:
# Write a recursive function to reverse a string.
#
# Test Cases:
# Input: "hello" → Output: "olleh"
# Input: "abc" → Output: "cba"
# --------------------------------------------------

def reverse_string(s):
    if s == "":
        return s
    return reverse_string(s[1:]) + s[0]

print(reverse_string("hello"))
print(reverse_string("abc"))
print()


# --------------------------------------------------
# 6. Fibonacci number
# Question:
# Write a recursive function to return the Nth Fibonacci number.
#
# Test Cases:
# Input: 6 → Output: 8
# Input: 4 → Output: 3
# --------------------------------------------------

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(6))
print(fibonacci(4))
print()


# --------------------------------------------------
# 7. Sum of digits
# Question:
# Write a recursive function to find the sum of digits of a number.
#
# Test Cases:
# Input: 123 → Output: 6
# Input: 405 → Output: 9
# --------------------------------------------------

def sum_of_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_of_digits(n // 10)

print(sum_of_digits(123))
print(sum_of_digits(405))
print()


# --------------------------------------------------
# 8. Count number of digits
# Question:
# Write a recursive function to count the number of digits in a number.
#
# Test Cases:
# Input: 456 → Output: 3
# Input: 12003 → Output: 5
# --------------------------------------------------

def count_digits(n):
    if n < 10:
        return 1
    return 1 + count_digits(n // 10)

print(count_digits(456))
print(count_digits(12003))
print()


# --------------------------------------------------
# 9. Power of a number (x^n)
# Question:
# Write a recursive function to calculate x raised to the power n.
#
# Test Cases:
# Input: x = 2, n = 3 → Output: 8
# Input: x = 5, n = 0 → Output: 1
# --------------------------------------------------

def power(x, n):
    if n == 0:
        return 1
    return x * power(x, n - 1)

print(power(2, 3))
print(power(5, 0))
print()


# --------------------------------------------------
# 10. GCD of two numbers
# Question:
# Write a recursive function to calculate the GCD of two numbers
# using Euclidean Algorithm.
#
# Test Cases:
# Input: 24, 18 → Output: 6
# Input: 10, 5 → Output: 5
# --------------------------------------------------

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

print(gcd(24, 18))
print(gcd(10, 5))
