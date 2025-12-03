# A dictionary in Python is an ordered, mutable collection that stores key-value pairs.

# Syntax of a Dictionary:
# dictionary_name = {key1: value1, key2: value2, key3: value3}

# Creating a dictionary:
student = {"name": "Satish", "Age": 22, "gender": "M"}
print(student)
# Output: {'name': 'Satish', 'Age': 22, 'gender': 'M'}

# Accessing Values
print(student["name"])      # -> Satish
print(student.get("name"))  # -> Satish

# Adding and updating:
student["college"] = "Govt College"
print(student)
# Output: {'name': 'Satish', 'Age': 22, 'gender': 'M', 'college': 'Govt College'}

# Removing items:
student.pop("Age")
print(student) #{'name': 'Satish', 'gender': 'M', 'college': 'Govt College'}

# Removes last item:
student.popitem()
print(student)  # {'name': 'Satish', 'gender': 'M'}

# Clear:
student.clear()
print(student)  # {}

# Dictionary Built-in Methods
student = {"name": "Satish", "Age": 22, "gender": "M"}
print(student.keys())       # dict_keys(['name', 'Age', 'gender'])
print(student.values())     # dict_values(['Satish', 22, 'M'])
print(student.items())      # dict_items([('name', 'Satish'), ('Age', 22), ('gender', 'M')])

# Dictionary Methods for Adding and Updating Data
student.update({
    "gender": "M",
    "phone": 123456,
    "college": "Govt College"
})
print(student)
# Output: {'name': 'Satish', 'Age': 22, 'gender': 'male', 'phone': 123456, 'college': 'Govt College'}

student.setdefault("city", "Rjy")
print(student['city'])  # Rjy

# Dictionary Methods for Removing Data
# pop:
print(student.pop("Age"))

# Using delete:
del student["gender"]
print(student)
# Output: {'name': 'Satish', 'phone': 123456, 'college': 'Govt College', 'city': 'Rjy'}

# Using popitem():
student.popitem()
print(student)
# Output: {'name': 'Satish', 'phone': 123456, 'college': 'Govt College'}

student.clear()
print(student)  # {}

# Dictionary comprehension:
squares = {x: x*x for x in range(1, 6)}
print(squares)
# Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}