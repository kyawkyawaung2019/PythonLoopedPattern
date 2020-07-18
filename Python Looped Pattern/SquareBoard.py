x = 5
y = 5
for row in range(x):
    for column in range(y):
        print('#' if row in [0, x-1] or column in [0, y-1] else '#', end = ' ')
    print()
