# 5. Second largest element
# Approach: Sort unique elements and pick second last.

nums = [3, 7, 2, 9, 5, 9]
print(sorted(set(nums))[-2])