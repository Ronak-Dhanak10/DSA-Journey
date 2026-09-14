n = 6
for i in range(1,n+1):
        
        char = 65 

        for k in range(n-i):
         print(" ", end=" ")

        for j in range(2 * i-1):
            print(chr(char), end=" ")
         
            if j<i-1:
                char+=1
            else:
                char-=1

        print()
