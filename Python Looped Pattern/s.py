for i in range(8):
    for col1 in range(1, i+2):
        if(col1 == 8):
            continue
        print(col1, end=" ")
    for col2 in range(13-i*2):
        print(" ", end=" ")
    for col2 in range(8+i-7, 0, -1):
        print(col2, end=" ")
    print()
