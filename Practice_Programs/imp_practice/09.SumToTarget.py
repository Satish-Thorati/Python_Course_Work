# 9. Pairs that sum to target
# Approach: Use hash set for O(n).

nums = [2, 7, 4, 5, 1, 3]
target = 6
seen = set()
for n in nums:
   if target - n in seen:
      print(n, target - n)
seen.add(n)