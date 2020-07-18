for i in range(8, 0, -1):
    for col1 in range(1, i+1):
        print(col1, end=" ")
    for col2 in range(15-i*2, 0, -1):
        print(" ", end=" ")
    for col2 in range(i, 0, -1):
        if(col2 == 8):
            continue
        print(col2, end=" ")
    print()
