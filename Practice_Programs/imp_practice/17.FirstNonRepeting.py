# 17. First non-repeating character
# Approach: Count and check order.

s = "swiss"
for ch in s:
    if s.count(ch) == 1:
        print(ch)
        break