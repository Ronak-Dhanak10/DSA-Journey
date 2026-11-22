# Armstrong number 
n = 153
num = n
nod = len(str(n))
total = 0
while n > 0:
    ld = n % 10
    total = total + ld** nod
    n //= 10
    print(total)
if num == total:
        print("Armstrong number")
else:
        print("Not an Armstrong number")
