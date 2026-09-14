n = 9
for i in range(1,2*n,2):
    stars = i if i <= n else 2*n - i

    for j in range(stars):
      print("*", end="")
    print()

    