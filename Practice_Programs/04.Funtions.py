#31. Check if Number is Prime
num = int(input("Enter a number: "))

if num <= 1:
    print("Is prime: False")
else:
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    print("Is prime:", is_prime)

#32. Count Vowels in a String
text = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0

for ch in text:
    if ch in vowels:
        count += 1

print("Number of vowels:", count)

#33. Multiply by 2 Using Lambda
num = int(input("Enter a number: "))
result = (lambda x: x * 2)(num)
print("Result:", result)

#34. Square List Using map() and Lambda
elements = list(map(int, input("Enter list elements: ").split()))
squared = list(map(lambda x: x ** 2, elements))
print("Squared list:", squared)

#35. Filter Even Numbers Using filter() and Lambda
elements = list(map(int, input("Enter list elements: ").split()))
even_numbers = list(filter(lambda x: x % 2 == 0, elements))
print("Even numbers:", even_numbers)

#36. Sort Tuples by Second Value Using Lambda
tuples = eval(input("Enter list of tuples: "))
sorted_list = sorted(tuples, key=lambda x: x[1])
print("Sorted list:", sorted_list)

#37. Access Global Variable Inside Function
message = "Hello"

def show_message():
    print("Global variable value is:", message)

show_message()


#38. Modify Global Variable Inside Function
message = "Hello"

def modify_message():
    global message
    message = "Changed"

modify_message()
print("Modified global variable is:", message)

#39. Use Local Variable with Same Name as Global
value = "Global"

def show_value():
    value = "Local"
    print("Inside function:", value)

show_value()
print("Outside function:", value)

#40. Compare Global and Local Variables
x = 10

def compare():
    x = 20
    print("Local x:", x)

print("Global x:", x)
compare()