# 19. Longest word in a sentence
# Approach: Use max() with key.

sentence = "Python makes coding simple and powerful"
print(max(sentence.split(), key=len))