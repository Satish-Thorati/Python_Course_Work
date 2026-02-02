#1. Triangle Type Checker
a = int(input("Enter side 1: "))
b = int(input("Enter side 2: "))
c = int(input("Enter side 3: "))

if a == b == c:
    print("Equilateral")
elif a == b or b == c or a == c:
    print("Isosceles")
else:
    print("Scalene")

#2. Character Classification
ch = input("Enter a character: ")

if ch.isalpha():
    if ch.lower() in 'aeiou':
        print("Vowel")
    else:
        print("Consonant")
elif ch.isdigit():
    print("Digit")
else:
    print("Special Character")

#3. BMI Calculator
height = float(input("Enter height in meters: "))
weight = float(input("Enter weight in kg: "))

bmi = weight / (height ** 2)

if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")

#4. Electricity Bill Calculator
units = int(input("Enter units consumed: "))

if units <= 100:
    bill = units * 1
elif units <= 200:
    bill = 100*1 + (units-100)*2
else:
    bill = 100*1 + 100*2 + (units-200)*3

print("Bill Amount: ₹", bill)

#5. Armstrong Number (3-digit)
num = int(input("Enter a number: "))
temp = num
sum = 0

while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10

if sum == num:
    print("Armstrong")
else:
    print("Not Armstrong")

#6. Strong Password Validator
password = input("Enter password: ")

if (len(password) >= 8 and
    any(c.isupper() for c in password) and
    any(c.isdigit() for c in password) and
    any(not c.isalnum() for c in password)):
    print("Strong Password")
else:
    print("Weak Password")

#7. ATM Withdrawal Simulation
balance = int(input("Enter balance: "))
withdraw = int(input("Enter withdrawal amount: "))

if withdraw < 500:
    print("Minimum withdrawal is 500")
elif withdraw % 100 != 0:
    print("Amount must be multiple of 100")
elif withdraw > balance:
    print("Insufficient Balance")
else:
    print("Success")

#8. Ticket Fare with Age Discount
age = int(input("Enter age: "))
fare = 100

if age < 5:
    fare = 0
elif age < 18:
    fare *= 0.5
elif age > 60:
    fare *= 0.7

print("Fare: ₹", int(fare))

#9. 24-Hour to 12-Hour Time Converter
hour, minute = map(int, input("Enter time (HH MM): ").split())

if hour == 0:
    print(f"12:{minute:02d} AM")
elif hour < 12:
    print(f"{hour}:{minute:02d} AM")
elif hour == 12:
    print(f"12:{minute:02d} PM")
else:
    print(f"{hour-12}:{minute:02d} PM")

##11. Grading System
marks = int(input("Enter marks: "))

if 90 <= marks <= 100:
    print("A")
elif 85 <= marks <= 89:
    print("B+")
elif 80 <= marks <= 84:
    print("B")
elif 70 <= marks <= 79:
    print("C")
else:
    print("F")

#12. Currency Denomination Counter
amount = int(input("Enter amount: "))
denominations = [2000, 500, 100, 50, 20, 10]

for d in denominations:
    count = amount // d
    if count > 0:
        print(f"{count} x {d}")
        amount %= d

#13. Movie Ticket Price
day = input("Enter day: ").lower()
age = int(input("Enter age: "))

if day in ["saturday", "sunday"]:
    price = 200
else:
    price = 150

if age < 12:
    price *= 0.5

print("Ticket Price: ₹", int(price))

#14. Angle Classification
angle = int(input("Enter angle: "))

if angle < 90:
    print("Acute")
elif angle == 90:
    print("Right")
elif angle < 180:
    print("Obtuse")
else:
    print("Straight")

#15. College Admission Decision
m1 = int(input("Enter marks 1: "))
m2 = int(input("Enter marks 2: "))
m3 = int(input("Enter marks 3: "))

avg = (m1 + m2 + m3) / 3

if avg > 90 and m1 > 70 and m2 > 70 and m3 > 70:
    print("Admitted")
elif avg > 80:
    print("Waitlisted")
else:
    print("Rejected")