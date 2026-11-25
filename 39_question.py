def numberofsteps(num):
    steps = 0
    for i in range(num):
        if num % 2 == 0:
            num = num // 2
        else:
            num = num - 1
        steps += 1
        return steps
numberofsteps(14)