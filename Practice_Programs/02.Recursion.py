"""
========================================
RECURSION PROGRAMS (11 – 20) – ONE SHEET
========================================
"""

# --------------------------------------------------
# 11. Maximum element in a list
# Question:
# Write a recursive function to find the maximum element in a list.
#
# Test Cases:
# Input: [3, 7, 2, 9, 5] → Output: 9
# Input: [1, 1, 1, 1] → Output: 1
# --------------------------------------------------

def find_max(lst):
    if len(lst) == 1:
        return lst[0]
    return max(lst[0], find_max(lst[1:]))

print(find_max([3, 7, 2, 9, 5]))
print(find_max([1, 1, 1, 1]))
print()


# --------------------------------------------------
# 12. Check if a list is a palindrome
# --------------------------------------------------

def is_list_palindrome(lst):
    if len(lst) <= 1:
        return True
    if lst[0] != lst[-1]:
        return False
    return is_list_palindrome(lst[1:-1])

print(is_list_palindrome([1, 2, 3, 2, 1]))
print(is_list_palindrome([1, 2, 3, 4]))
print()


# --------------------------------------------------
# 13. Binary Search (Recursive)
# --------------------------------------------------

def binary_search(arr, low, high, target):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif target < arr[mid]:
        return binary_search(arr, low, mid - 1, target)
    else:
        return binary_search(arr, mid + 1, high, target)

arr1 = [1, 3, 5, 7, 9]
print(binary_search(arr1, 0, len(arr1) - 1, 5))

arr2 = [2, 4, 6, 8]
print(binary_search(arr2, 0, len(arr2) - 1, 7))
print()


# --------------------------------------------------
# 14. Sum of list elements
# --------------------------------------------------

def sum_list(lst):
    if not lst:
        return 0
    return lst[0] + sum_list(lst[1:])

print(sum_list([1, 2, 3, 4]))
print(sum_list([10, -2, 5]))
print()


# --------------------------------------------------
# 15. Count occurrences of a number in a list
# --------------------------------------------------

def count_occurrences(lst, x):
    if not lst:
        return 0
    return (1 if lst[0] == x else 0) + count_occurrences(lst[1:], x)

print(count_occurrences([1, 2, 1, 3, 1], 1))
print(count_occurrences([4, 5, 6], 2))
print()


# --------------------------------------------------
# 16. Permutations of a string
# --------------------------------------------------

def permutations(s, ans=""):
    if len(s) == 0:
        print(ans)
        return
    for i in range(len(s)):
        permutations(s[:i] + s[i+1:], ans + s[i])

permutations("abc")
print()
permutations("ab")
print()


# --------------------------------------------------
# 17. Replace all occurrences of a character
# --------------------------------------------------

def replace_char(s, old, new):
    if s == "":
        return s
    if s[0] == old:
        return new + replace_char(s[1:], old, new)
    return s[0] + replace_char(s[1:], old, new)

print(replace_char("abab", 'a', 'x'))
print(replace_char("hello", 'l', 'z'))
print()


# --------------------------------------------------
# 18. Convert number to binary using recursion
# --------------------------------------------------

def to_binary(n):
    if n == 0:
        return ""
    return to_binary(n // 2) + str(n % 2)

print(to_binary(5))
print(to_binary(8))
print()


# --------------------------------------------------
# 19. Check if a string is a palindrome
# --------------------------------------------------

def is_string_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_string_palindrome(s[1:-1])

print(is_string_palindrome("madam"))
print(is_string_palindrome("hello"))
print()


# --------------------------------------------------
# 20. Find first index of element in list
# --------------------------------------------------

def first_index(lst, x, index=0):
    if index == len(lst):
        return -1
    if lst[index] == x:
        return index
    return first_index(lst, x, index + 1)

print(first_index([1, 2, 3, 2, 5], 2))
print(first_index([4, 5, 6], 1))
