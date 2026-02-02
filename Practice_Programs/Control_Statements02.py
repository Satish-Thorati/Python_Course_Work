#16. Print Numbers from N to 1 (Using while loop)
N = int(input("Enter N: "))
while N >= 1:
    print(N)
    N -= 1

#17. Find Sum of Prime Numbers up to N (Using for loop)
N = int(input("Enter N: "))
sum_primes = 0

for num in range(2, N + 1):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        sum_primes += num

print("Sum of prime numbers:", sum_primes)

#18. Find the Product of Digits of a Number (Using while loop)
n = int(input("Enter number: "))
product = 1

while n > 0:
    digit = n % 10
    product *= digit
    n //= 10

print("Product of digits:", product)

#19. Print Numbers Divisible by Both 3 and 5 (Using for loop)
N = int(input("Enter N: "))
for i in range(1, N + 1):
    if i % 3 == 0 and i % 5 == 0:
        print(i)

#20. Find GCD of Two Numbers (Using while loop)
a = int(input("Enter a: "))
b = int(input("Enter b: "))

while b != 0:
    a, b = b, a % b

print("GCD:", a)

#21. Print Right-Angled Triangle Pattern (Using for loop)
N = int(input("Enter N: "))
for i in range(1, N + 1):
    print("*" * i)

#22. Print Hollow Square Pattern (Using for loop)
N = int(input("Enter N: "))
for i in range(1, N + 1):
    if i == 1 or i == N:
        print("* " * N)
    else:
        print("* " + "  " * (N - 2) + "*")

#23. Check if a Number is Perfect (Using for loop)
N = int(input("Enter N: "))
sum = 0

for i in range(1, N):
    if N % i == 0:
        sum += i

if sum == N:
    print("Perfect")
else:
    print("Not Perfect")

#24. Count Digits in a Number (Using while loop)
n = int(input("Enter number: "))
count = 0

while n > 0:
    count += 1
    n //= 10

print("Number of digits:", count)

#25. Print Numbers Divisible by 7 (Using for loop)
N = int(input("Enter N: "))
for i in range(1, N + 1):
    if i % 7 == 0:
        print(i)

#26. Find the LCM of Two Numbers (Using while loop)
a = int(input("Enter a: "))
b = int(input("Enter b: "))

max_num = max(a, b)

while True:
    if max_num % a == 0 and max_num % b == 0:
        print("LCM:", max_num)
        break
    max_num += 1

#27. Print Even Numbers in Reverse Order (Using while loop)
N = int(input("Enter N: "))
while N >= 1:
    if N % 2 == 0:
        print(N)
    N -= 1

#28. Sum of First N Odd Numbers (Using for loop)
N = int(input("Enter N: "))
sum = 0

for i in range(1, 2 * N, 2):
    sum += i

print("Sum of first N odd numbers:", sum)

#29. Print a Square Pattern of Numbers (Using for loop)
N = int(input("Enter N: "))
for i in range(1, N + 1):
    for j in range(1, N + 1):
        print(j, end=" ")
    print()

#30. Check if a Number is Armstrong (Using for loop)
n = int(input("Enter number: "))
temp = n
sum = 0
digits = len(str(n))

for digit in str(n):
    sum += int(digit) ** digits

if sum == temp:
    print("Armstrong")
else:
    print("Not Armstrong")