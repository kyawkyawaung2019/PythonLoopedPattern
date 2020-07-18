for i in range(1, 9):
    print()
    for j in range(12 - i):
        print(" "*2, end="  ")
    for i in range(0, i, 1):
        print('{:>3}'.format(2**i), end=" ")
    for i in range(-1+i, -1, -1):
        print('{:>3}'.format(2**i), end=" ")
    print(" ")
