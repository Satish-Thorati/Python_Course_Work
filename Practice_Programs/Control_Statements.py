#1. Print Numbers from 1 to N (Using for loop)
N = int(input("Enter N: "))
for i in range(1, N + 1):
    print(i)

#2. Print Even Numbers from 1 to N (Using for loop)
N = int(input("Enter N: "))
for i in range(1, N + 1):
    if i % 2 == 0:
        print(i)

#3. Sum of Numbers from 1 to N (Using for loop)
N = int(input("Enter N: "))
sum = 0
for i in range(1, N + 1):
    sum += i
print("Sum:", sum)

#4. Print Odd Numbers from 1 to N (Using for loop)
N = int(input("Enter N: "))
for i in range(1, N + 1):
    if i % 2 != 0:
        print(i)

#5. Find Factorial of a Number (Using for loop)
N = int(input("Enter N: "))
fact = 1
for i in range(1, N + 1):
    fact *= i
print("Factorial:", fact)

#6. Print Multiplication Table of N (Using for loop)
N = int(input("Enter N: "))
for i in range(1, 11):
    print(N, "x", i, "=", N * i)

#7. Check Prime Number (Using for loop)
N = int(input("Enter N: "))
count = 0
for i in range(1, N + 1):
    if N % i == 0:
        count += 1
if count == 2:
    print("Prime")
else:
    print("Not Prime")

#8. Sum of Digits of a Number (Using while loop)
n = int(input("Enter number: "))
sum = 0

while n > 0:
    digit = n % 10
    sum += digit
    n //= 10
print("Sum of digits:", sum)

#9. Print Fibonacci Sequence up to N Terms (Using for loop)
N = int(input("Enter N: "))
a, b = 0, 1
for i in range(N):
    print(a)
    a, b = b, a + b

#10. Count Numbers Divisible by 3 (Using for loop)
N = int(input("Enter N: "))
count = 0
for i in range(1, N + 1):
    if i % 3 == 0:
        count += 1

print("Count:", count)

#11. Check if a Number is Palindrome (Using while loop)
n = int(input("Enter number: "))
temp = n
rev = 0

while n > 0:
    rev = rev * 10 + (n % 10)
    n //= 10

if temp == rev:
    print("Palindrome")
else:
    print("Not Palindrome")

#12. Print Multiples of 5 up to N (Using for loop)
N = int(input("Enter N: "))
for i in range(1, N + 1):
    if i % 5 == 0:
        print(i)

#13. Find the Maximum of Three Numbers (Using for loop)
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

max_num = a
for num in [b, c]:
    if num > max_num:
        max_num = num

print("Maximum:", max_num)

#14. Print Reverse of a Number (Using while loop)
n = int(input("Enter number: "))
rev = 0

while n > 0:
    rev = rev * 10 + (n % 10)
    n //= 10

print("Reverse:", rev)

#15. Sum of First N Natural Numbers (Using for loop)
N = int(input("Enter N: "))
sum = 0

for i in range(1, N + 1):
    sum += i

print("Sum:", sum)