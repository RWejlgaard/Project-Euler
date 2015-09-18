lst = []
for x in range(100, 1000):
	for y in range(100, 1000):
		z = str(x*y)
		if z == z[::-1] and z not in lst:
			lst.append(z)
lst.sort(key=int)
print lst
