# 10. Missing number in 1 to n
# Approach: Use sum formula.

nums = [1, 2, 3, 5]
n = 5
print(n*(n+1)//2 - sum(nums))