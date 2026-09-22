# Write a Python program to print your name 100 times using recursion.
def name(i,n):
    # na = input("Enter your name: ")
    if i> n:
        return
    print("Ronak")
    name(i+1,n)
# na = input("Enter your name: ")
n = int(input("Enter the number of times to print the name: "))
name(1,n)

# name = input("Enter the name:")
# for i in range(1,100):
#     print(name)
