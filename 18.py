lst = []
with open('18.txt') as infile:
	for line in infile:
		lst.append(line.strip().split())

for a in range(0, 15):
	for b in range(0, len(lst[a])):
		lst[a][b] = int(lst[a][b])

for a in range(1, 15):
	for b in range(0, len(lst[a])):
		x = 0
		y = 0
		if b == 0:
			y = lst[a - 1][b]
			lst[a][b] = lst[a][b] + y
		elif b == len(lst[a]) - 1:
			x = lst[a - 1][b - 1]
			lst[a][b] = lst[a][b] + x
		else:
			x = lst[a - 1][b - 1]
			y = lst[a - 1][b]
			lst[a][b] = lst[a][b] + max(x, y)
print max(lst[14])