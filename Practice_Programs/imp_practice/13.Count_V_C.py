# 13. Count vowels and consonants
# Approach: Simple iteration.

s = "hello world"
vowels = "aeiouAEIOU"
v = sum(1 for ch in s if ch in vowels)
c = sum(1 for ch in s if ch.isalpha() and ch not in vowels)
print("Vowels:", v, "Consonants:", c)