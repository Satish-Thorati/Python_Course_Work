# 11. Move zeros to end
# Approach: Keep non-zeros, then append zeros.

nums = [0, 1, 0, 3, 12]
nums = [x for x in nums if x != 0] + [0]*nums.count(0)
print(nums)