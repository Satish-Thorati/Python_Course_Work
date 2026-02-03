#16. Check if a number is perfect
num = int(input("Enter a number: "))
sum_div = sum(i for i in range(1, num) if num % i == 0)
if sum_div == num:
    print("Perfect")
else:
    print("Not Perfect")

#17. Identify type of triangle by angles
a, b, c = map(int, input("Enter three angles: ").split())
if a + b + c != 180:
    print("Not a valid triangle")
elif 90 in [a, b, c]:
    print("Right")
elif all(angle < 90 for angle in [a, b, c]):
    print("Acute")
else:
    print("Obtuse")

#18. Convert marks to 10-point GPA
marks = int(input("Enter marks (0-100): "))
if 91 <= marks <= 100:
    gpa = 10
elif 81 <= marks <= 90:
    gpa = 9
elif 71 <= marks <= 80:
    gpa = 8
elif 61 <= marks <= 70:
    gpa = 7
elif 51 <= marks <= 60:
    gpa = 6
elif 41 <= marks <= 50:
    gpa = 5
else:
    gpa = 0
print("GPA:", gpa)

#19. Check if four digits form a lucky number
num = input("Enter a 4-digit number: ")
if len(num) == 4 and int(num[0]) + int(num[1]) == int(num[2]) + int(num[3]):
    print("Lucky")
else:
    print("Not Lucky")

#20. Car insurance premium
age, exp = map(int, input("Enter age and experience: ").split())
if age < 25 and exp < 3:
    print("High Risk")
elif age > 25 and exp > 5:
    print("Low Risk")
else:
    print("Medium Risk")

#21. Ticket system for amusement park
age = int(input("Enter age: "))
if age < 12:
    price = 50
elif age < 60:
    price = 100
else:
    price = 60
print(f"₹{price}")

#22. Classify number as Single, Double, or Triple digit
num = int(input("Enter a number: "))
if 0 <= num <= 9:
    print("Single Digit")
elif 10 <= num <= 99:
    print("Double Digit")
elif 100 <= num <= 999:
    print("Triple Digit")
else:
    print("More than 3 digits")

#23. Validate time input (HH:MM format)
time = input("Enter time (HH:MM): ")
try:
    hh, mm = map(int, time.split(":"))
    if 0 <= hh <= 23 and 0 <= mm <= 59:
        print("Valid")
    else:
        print("Invalid")
except:
    print("Invalid")

#24. Weather categorization by temperature
temp = float(input("Enter temperature: "))
if temp < 10:
    print("Very Cold")
elif 10 <= temp <= 20:
    print("Cold")
elif 21 <= temp <= 30:
    print("Warm")
else:
    print("Hot")

#25. Assign mobile plan based on usage
usage = float(input("Enter usage in GB: "))
if usage < 1:
    plan = "Plan A"
elif usage < 5:
    plan = "Plan B"
else:
    plan = "Plan C"
print(plan)

#26. Identify duplicate digits in a 3-digit number
num = input("Enter a 3-digit number: ")
if len(set(num)) < 3:
    print("Duplicates Present")
else:
    print("Unique Digits")

#27. Weekday classifier
day = int(input("Enter day number (1-7): "))
days = {
    1: "Monday - Weekday",
    2: "Tuesday - Weekday",
    3: "Wednesday - Weekday",
    4: "Thursday - Weekday",
    5: "Friday - Weekday",
    6: "Saturday - Weekend",
    7: "Sunday - Weekend"
}
print(days.get(day, "Invalid day"))

#28. Student attendance eligibility
attended, total = map(int, input("Enter classes attended and total: ").split())
percent = (attended / total) * 100
if percent > 75:
    print("Eligible")
else:
    print("Not Eligible")

#29. Print grade trend
s1, s2, s3 = map(int, input("Enter three scores: ").split())
if s1 < s2 < s3:
    print("Improving")
elif s1 > s2 > s3:
    print("Declining")
else:
    print("Fluctuating")

#30. Validate mobile number
num = input("Enter mobile number: ")
if len(num) == 10 and num[0] in "6789" and num.isdigit():
    print("Valid")
else:
    print("Invalid")