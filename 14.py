from datetime import datetime
start = datetime.now()

x = 0
y = 0
z = 0
h = 0
for a in xrange(1, 1000000):
	x = a
	while x != 1:
		if x % 2 == 0:
			x /= 2
		else:
			x = 3*x + 1
		y += 1
	if z < y:
		z = y
		h = a
	y = 0
print h
print z
print datetime.now() - start