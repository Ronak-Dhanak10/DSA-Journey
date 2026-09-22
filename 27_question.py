# factorial of a number using recursion
def factorial(i):
    if i == 0:
        return 1
    return i * factorial(i - 1)

i = 6
print("Factorial of", i, "is:", factorial(i))