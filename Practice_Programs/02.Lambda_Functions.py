from functools import reduce
# 11. Check if string starts with a vowel using lambda
starts_with_vowel = lambda s: s[0].lower() in 'aeiou'
print(starts_with_vowel("apple"))    # True
print(starts_with_vowel("banana"))   # False


# 12. Add 10 to each element using lambda and map()
nums1 = [1, 2, 3]
nums2 = [5, 0, -2]
print(list(map(lambda x: x + 10, nums1)))
print(list(map(lambda x: x + 10, nums2)))


# 13. Filter strings longer than 3 characters
words1 = ["a", "the", "lamp", "cat"]
words2 = ["sun", "sky", "tree"]
print(list(filter(lambda x: len(x) > 3, words1)))
print(list(filter(lambda x: len(x) > 3, words2)))


# 14. Multiply each number by its index using lambda
nums3 = [1, 2, 3, 4]
nums4 = [5, 6, 7]
print(list(map(lambda x: x[0] * x[1], enumerate(nums3))))
print(list(map(lambda x: x[0] * x[1], enumerate(nums4))))


# 15. Use lambda with reduce() to calculate product
print(reduce(lambda a, b: a * b, [1, 2, 3, 4]))  # 24
print(reduce(lambda a, b: a * b, [2, 5, 5]))     # 50


# 16. Use lambda with filter to find multiples of 3
nums5 = [1, 3, 4, 6, 9]
nums6 = [5, 10, 12, 15]
print(list(filter(lambda x: x % 3 == 0, nums5)))
print(list(filter(lambda x: x % 3 == 0, nums6)))


# 17. Sort words in a list by their length
words3 = ["car", "elephant", "cat"]
words4 = ["hi", "world", "python"]
print(sorted(words3, key=lambda x: len(x)))
print(sorted(words4, key=lambda x: len(x)))


# 18. Lambda to extract domain from email
get_domain = lambda email: email.split('@')[1]
print(get_domain("user@gmail.com"))
print(get_domain("name@yahoo.com"))


# 19. Use lambda to get last digit of a number
last_digit = lambda n: n % 10
print(last_digit(123))   # 3
print(last_digit(7890))  # 0


# 20. Use lambda to check if year is a leap year
is_leap_year = lambda y: (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)
print(is_leap_year(2020))  # True
print(is_leap_year(2023))  # False