k=1
l=4
m=1
n=1
for i in range(0, 7):
    for j in range(0, 7):
        if i==0 or i==6:
            print("#", end=" ")
        elif i==n and j==m and i==k:
            print("#", end=" ")
            n=n+1
            m=m+1
        elif i==k and j==l:
            print("  #", end=" ")
            k=k+1
            l=l-1
        elif i==5 and j==4:
            print("#", end=" ")
        elif i==4 and j==3:
            print("#", end=" ")
        else:
            print(end="  ")
    print()
