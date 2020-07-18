num = 8
for i in range(num):
	spaces = i
	row = [j+1 for j in range(num-i)]+[(num-i-1)-j for j in range(num-i-1)]
	rowstring=' '.join(map(str, row))
	for j in range(spaces):
		rowstring=' '+' '+rowstring
	print(rowstring)