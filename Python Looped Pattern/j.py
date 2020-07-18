#h = eval(input("please enter diamond's height:"))
h = 7

for i in range(h-2, -1, -1):
    print()
    print("  "*(h-i), " #"*(i*2+1))
