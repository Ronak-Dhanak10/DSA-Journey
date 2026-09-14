def armstrong_number(num):
    sum = 0
    
    temp = num
    digits = len(str(num))

    while temp > 0:
        digit = temp%10
        sum = sum + digit**digits
        temp //= 10
    if num == sum:
        return True
    else:
        return False
result = armstrong_number(int(input("Enter a number: ")))
print(result)