# DSA question 1 
# Count the digit in a number
n = 3524975
num = n 
count = 0 
while num > 0:
    num = num // 10
    count += 1
print(count)

# Time complexity: O(log n) where n is the input number
# Space complexity: O(1)