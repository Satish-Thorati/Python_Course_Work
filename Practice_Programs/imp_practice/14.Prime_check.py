# 14. Check if number is prime
# Approach: Check divisibility till √n.

n = 29
if n < 2:
   print(False)
else:
   for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            print(False)
            break

        else:
            print(True)