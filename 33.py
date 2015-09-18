lst = []

for x in range(10, 99):
	for y in range(x + 1, 100):
		x2 = str(x)
		y2 = str(y)
		if x2[1] != "0" and y2[1] != "0":
			if x2[0] == y2[0]:
				x2 = float(x2[1])
				y2 = float(y2[1])

				if x / x2 == y / y2:
					for z in range(x, 2, -1):
						if (x / z).is_integer() and (y / z).is_integer():
							lst.append(x / z)
							lst.append(y / z)
							break

			elif x2[0] == y2[1] and y2[0] != "0":
				x2 = float(x2[1])
				y2 = float(y2[0])

				if x / x2 == y / y2:
					for z in range(x, 2, -1):
						if (x / z).is_integer() and (y / z).is_integer():
							lst.append(x / z)
							lst.append(y / z)
							break
					
			elif x2[1] == y2[0] and x2[0] != "0":
				x2 = float(x2[0])
				y2 = float(y2[1])

				if x / x2 == y / y2:
					for z in range(x, 2, -1):
						if (x / z).is_integer() and (y / z).is_integer():
							lst.append(x / z)
							lst.append(y / z)
							break
					
			elif x2[1] == y2[1] and x2[0] != "0" and y2[0] != "0":
				x2 = float(x2[0])
				y2 = float(y2[0])

				if x / x2 == y / y2:
					for z in range(x, 2, -1):
						if (x / z).is_integer() and (y / z).is_integer():
							lst.append(x / z)
							lst.append(y / z)
							break
n = 1.0
d = 1.0
for x in range(0, len(lst), 2):
	n *= lst[x]
for x in range(1, len(lst), 2):
	d *= lst[x]
for x in range(int(n), 1, -1):
	if (n / x).is_integer() and (d / x).is_integer():
		d = d / x
		break
print(d)