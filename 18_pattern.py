n = 5
space = 0
for i in range(1, n+1):
    for j in range(1, i + 1):
        print("*", end="")

    for j in range(space):
        print(" ", end="")

    for j in range(i, 0, -1):
        print("*", end="")
    space += 2
    print()

space = 8
for i in range(n-1, 0, -1):
    for j in range(1, i + 1):
        print("*", end="")

    for j in range(space):
        print(" ", end="")

    for j in range(i, 0, -1):
        print("*", end="")
    space -= 2
    print()

   