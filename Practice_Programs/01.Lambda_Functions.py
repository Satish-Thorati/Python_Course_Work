# 1. Square of a number using lambda
square = lambda x: x * x
print(square(4))   # 16
print(square(7))   # 49


# 2. Check if number is even using lambda
is_even = lambda x: x % 2 == 0
print(is_even(6))  # True
print(is_even(5))  # False


# 3. Get maximum of two numbers using lambda
maximum = lambda a, b: a if a > b else b
print(maximum(4, 9))  # 9
print(maximum(7, 3))  # 7


# 4. Multiply two numbers using lambda
multiply = lambda a, b: a * b
print(multiply(2, 5))  # 10
print(multiply(4, 3))  # 12


# 5. Sort a list of tuples by second element using lambda
data1 = [(1, 3), (2, 1), (4, 2)]
data2 = [(5, 10), (3, 7), (8, 1)]
print(sorted(data1, key=lambda x: x[1]))
print(sorted(data2, key=lambda x: x[1]))


# 6. Filter even numbers from a list using lambda and filter()
nums1 = [1, 2, 3, 4, 5, 6]
nums2 = [10, 15, 22]
print(list(filter(lambda x: x % 2 == 0, nums1)))
print(list(filter(lambda x: x % 2 == 0, nums2)))


# 7. Square each element in a list using lambda and map()
nums3 = [1, 2, 3]
nums4 = [4, 5, 6]
print(list(map(lambda x: x * x, nums3)))
print(list(map(lambda x: x * x, nums4)))


# 8. Convert list of strings to uppercase using lambda
words1 = ["hello", "world"]
words2 = ["python", "lambda"]
print(list(map(lambda x: x.upper(), words1)))
print(list(map(lambda x: x.upper(), words2)))


# 9. Sort list of dictionaries by key using lambda
people1 = [{'name': 'A', 'age': 30}, {'name': 'B', 'age': 20}]
people2 = [{'age': 25}, {'age': 18}]
print(sorted(people1, key=lambda x: x['age']))
print(sorted(people2, key=lambda x: x['age']))


# 10. Return length of a string using lambda
string_length = lambda s: len(s)
print(string_length("hello"))   # 5
print(string_length("python"))  # 6
