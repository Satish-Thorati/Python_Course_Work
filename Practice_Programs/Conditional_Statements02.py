## **21–40 (Advanced Conditionals)**

### 21. 4-Digit Even Number
n = 2468
if 1000 <= n <= 9999 and n % 2 == 0:
    print("4-digit even number")

### 22. Consonant Check
ch = 'b'
if ch.isalpha() and ch.lower() not in 'aeiou':
    print("Consonant")

### 23. Divisible by 2 or 3
n = 6
if n % 2 == 0 and n % 3 == 0:
    print("Divisible by both 2 and 3")
elif n % 2 == 0:
    print("Divisible by 2 only")
elif n % 3 == 0:
    print("Divisible by 3 only")

### 24. Negative and Odd
n = -5
if n < 0 and n % 2 != 0:
    print("Negative and odd number")

### 25. String Starts with Vowel
s = "apple"
if s[0].lower() in 'aeiou':
    print("Starts with a vowel")

### 26. Valid Triangle
a, b, c = 3, 4, 5
if a + b > c and a + c > b and b + c > a:
    print("Valid triangle")
else:
    print("Invalid triangle")

### 27. Greatest of Three Numbers
a, b, c = 12, 45, 30
print(max(a, b, c), "is the greatest")

### 28. Century Leap Year
year = 2000
if year % 100 == 0 and year % 400 == 0:
    print("Century leap year")

### 29. Digit Check
ch = '5'
if ch.isdigit():
    print("Digit")

### 30. Palindrome Number
n = 121
if str(n) == str(n)[::-1]:
    print("Palindrome number")

### 31. Compare String Length
s1, s2 = "cat", "mouse"
if len(s1) > len(s2):
    print("First string is longer")
else:
    print("Second string is longer")

### 32. Range & Divisible by 5
n = 75
if 50 <= n <= 100 and n % 5 == 0:
    print("In range and divisible by 5")

### 33. Strong Password
pwd = "secure123"
if len(pwd) >= 8:
    print("Strong password")
else:
    print("Weak password")

### 34. Sum is Even
a, b = 12, 16
if (a + b) % 2 == 0:
    print("Sum is even")

### 35. Special Character
ch = '@'
if not ch.isalnum():
    print("Special character")

### 36. Temperature Category
temp = 10
if temp < 15:
    print("Cold")
elif temp <= 30:
    print("Moderate")
else:
    print("Hot")

### 37. Outside Range 10–50
n = 55
if n < 10 or n > 50:
    print("Outside the range")

### 38. Perfect Square

n = 36
if int(n ** 0.5) ** 2 == n:
    print("Perfect square")

### 39. Compare Two Ages

a, b = 22, 25
if a > b:
    print("First person is older")
elif b > a:
    print("Second person is older")
else:
    print("Same age")


### 40. Angle Type
angle = 90
if angle < 90:
    print("Acute angle")
elif angle == 90:
    print("Right angle")
else:
    print("Obtuse angle")

