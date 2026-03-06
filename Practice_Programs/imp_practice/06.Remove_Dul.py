# 6. Remove duplicates from list
# Approach: Use set (fastest), but loses order; use dict for ordered.

nums = [1, 2, 2, 3, 4, 4]
print(list(dict.fromkeys(nums))) # preserves order