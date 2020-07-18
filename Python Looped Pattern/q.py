for i in range(1, 9):
    for j in range(9-i):
        print(" ", end=" ")
		
    for j in range(1, i):
        print(j, end=" ")
		
    for i in range(i, 0, -1):
        print(i, end=" ")
    print("\n")
