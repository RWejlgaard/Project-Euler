x = 1
y = 2
z = 0
s = 2
while (x < 4000000 and y < 4000000):
	if (z == 0):
		x = x + y
		if ((x % 2) == 0):
			s += x
		z = 1
	if (z == 1):
		y = x + y
		if ((y % 2) == 0):
			s += y
		z = 0
print s
