n = 5

for i in range(1, n + 1):
    char = 70-i
    for j in range(1, i + 1):
        print(chr(char), end=" ")
        char += 1
    print()
