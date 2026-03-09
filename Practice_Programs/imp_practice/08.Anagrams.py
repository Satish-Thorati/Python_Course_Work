# 8. Check if two strings are anagrams
# Approach: Compare sorted strings.

s1, s2 = "listen", "silent"
print(sorted(s1) == sorted(s2))
