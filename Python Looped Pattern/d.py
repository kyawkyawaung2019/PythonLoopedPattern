for row in range(0, 9):
    for column in range(8, row-1, -1):
        print(" ", end=" ")
        if row == column:
            print(" #"*row, end=" ")
    print()
   