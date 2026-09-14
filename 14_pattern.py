n = 5
for i in range(n,0,-1):
    char = 65
    for j in range(1,i+1):
        print(chr(char),end=" ")
        char+=1
    print()

