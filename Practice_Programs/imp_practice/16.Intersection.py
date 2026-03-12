# 16. Common elements between lists
# Approach: Convert both to sets.

a = [1, 2, 3, 4]
b = [2, 4, 6]
print(list(set(a).intersection(b)))