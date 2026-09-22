# using parameter
def sum_of_num(i, sum):
    if i <1:
        print("Sum of numbers is:", sum)
        return
    sum_of_num(i-1, sum+i)
no = int(input("Enter a number: "))
sum_of_num(no, 0)
