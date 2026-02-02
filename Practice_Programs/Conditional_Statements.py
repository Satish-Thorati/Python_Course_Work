

## **1–20 (Basics)**

### 1. Positive or Negative
n = 5
if n > 0:
    print("Positive number")
else:
    print("Negative number")

### 2. Even or Odd
n = 8
if n % 2 == 0:
    print("Even number")
else:
    print("Odd number")

### 3. Divisible by 5
n = 15
if n % 5 == 0:
    print("Divisible by 5")
else:
    print("Not divisible by 5")

### 4. Divisible by 3 and 7
n = 21
if n % 3 == 0 and n % 7 == 0:
    print("Divisible by both 3 and 7")
else:
    print("Not divisible by both")

### 5. Leap Year

year = 2024
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year")
else:
    print("Not a leap year")

### 6. Pass or Fail
marks = 40
if marks >= 35:
    print("Pass")
else:
    print("Fail")

### 7. 3-Digit Number
n = 123
if 100 <= abs(n) <= 999:
    print("3-digit number")
else:
    print("Not a 3-digit number")

### 8. Vowel Check
ch = 'a'
if ch.lower() in 'aeiou':
    print("Vowel")
else:
    print("Consonant")

### 9. Greatest of Two Numbers
a, b = 7, 9
if a > b:
    print(a, "is greater")
else:
    print(b, "is greater")

### 10. Smallest of Two Numbers
a, b = 3, 8
if a < b:
    print(a, "is smaller")
else:
    print(b, "is smaller")

### 11. Check Zero
n = 0
if n == 0:
    print("Number is zero")
else:
    print("Number is not zero")

### 12. Multiple of 10
n = 50
if n % 10 == 0:
    print("Multiple of 10")
else:
    print("Not a multiple of 10")

### 13. Eligible to Vote
age = 19
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible")

### 14. Between 1 and 100
n = 45
if 1 <= n <= 100:
    print("In range")
else:
    print("Out of range")

### 15. Square Check
a, b = 4, 2
if a == b * b:
    print("4 is square of 2")
else:
    print("Not a square")

### 16. String Equality
s1, s2 = "apple", "apple"
if s1 == s2:
    print("Strings are equal")
else:
    print("Strings are not equal")

### 17. Prime Number
n = 7
if n > 1:
    for i in range(2, n):
        if n % i == 0:
            print("Not prime")
            break
    else:
        print("Prime number")
else:
    print("Not prime")

### 18. Positive and Even
n = 12
if n > 0 and n % 2 == 0:
    print("Positive and even number")
else:
    print("Condition not satisfied")

### 19. Uppercase Letter
ch = 'A'
if ch.isupper():
    print("Uppercase letter")
else:
    print("Not uppercase")

### 20. Hot Temperature
temp = 35
if temp > 30:
    print("It's hot")
else:
    print("Not hot")

