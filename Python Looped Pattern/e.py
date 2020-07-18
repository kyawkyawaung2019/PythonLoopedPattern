row = 7
column = 7
for x in range(row):
    for y in range(column):
        print('#' if x in [0, column-1] or y in [0, row-1] else ' ', end = ' ')
    print()
