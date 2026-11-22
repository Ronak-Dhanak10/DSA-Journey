# Brute force approach to find all divisors of a number
n = 5000
les = []
for i in range(1, n + 1):
    if n % i == 0:
        les.append(i)
print(les)
# Time complexity: O(n)
# Space complexity: O(K) where K is the number of divisors of n)

#optimal approach to find all divisors of a number
import math
n = 5000
les = []
for i in range(1, int(math.sqrt(n)) + 1):
    if n % i == 0:
        les.append(i)
        if n // i != i:
            les.append(n // i)
print(les)