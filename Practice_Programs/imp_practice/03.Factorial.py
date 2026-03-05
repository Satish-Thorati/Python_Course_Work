# 3. Factorial of a number
# Approach 1 (Iterative):

n = 5
fact = 1
for i in range(1, n+1):
  fact *= i
print(fact)

#Approach 2 (Recursive):

def fact(n):
   return 1 if n == 0 else n * fact(n-1)
print(fact(5))