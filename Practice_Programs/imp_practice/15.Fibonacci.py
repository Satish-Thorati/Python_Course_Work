# 15. Fibonacci sequence
# Approach: Iterative generation.

n = 7
a, b = 0, 1
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b