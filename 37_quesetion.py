# Head Recursion
def funct(N):
    if 1 > N:
        return
    funct(N-1)
    print(N)
funct(5)
    