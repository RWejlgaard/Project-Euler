x = 1
a = 3
c = 0
q = 2

while a <= 1002001:
	c += 1
	if c == 4:
		q += 2
		c = 0
	x += a
	a += q
print x