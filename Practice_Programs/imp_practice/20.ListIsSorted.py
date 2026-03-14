# 20. Check if list is sorted
# Approach: Compare with sorted version.

nums = [1, 2, 3, 4, 5]
print(nums == sorted(nums) or nums == sorted(nums,
reverse=True))