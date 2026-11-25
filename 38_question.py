# Tail recursion
def funct(i,N):
    if i > N:
        return
    print(i)
    funct(i+1, N)
funct(1,10)
