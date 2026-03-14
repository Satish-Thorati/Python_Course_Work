# 21. Write a program to find maximum and minimum 
# without using built-in functions.

numbers = [10,20,5,8,30]

max_num = min_num = numbers[0]

for n in numbers:

    if n > max_num: 
        max_num = n

    if n < min_num:
        min_num = n

print("Max:", max_num)

print("Min:", min_num)