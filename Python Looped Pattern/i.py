a=1
b=5
c=4
d=2
m=1
n=1
for i in range(0, 7):
    for j in range(0, 7):
        if i==0 or i==6 or j==0 or j==6:
            print("#", end=" ")
        elif i==n and j==m:
            print("#", end=" ")
            n=n+1
            m=m+1
        elif i==a and j==b:
            print("#", end=" ")
            a=a+1
            b=b-1
        elif i==c and j==d:
            print("#", end=" ")
            c=c+1
            d=d-1
        else:
            print(end="  ")
    print()
