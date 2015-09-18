
for c in xrange(1000, 2, -1):
	for b in xrange(c, 2, -1):
		for a in xrange(b, 2, -1):
			if a**2 + b**2 == c**2 and a + b + c == 1000:
				print a, b, c
	if c % 100 == 0:
		print c