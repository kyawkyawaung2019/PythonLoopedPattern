for i in range(1, 9):
    for j in range(i):
        print(" ", end=" ")
    for k in range(8, i-1, -1):
        print('#', end=' ')
    print()
