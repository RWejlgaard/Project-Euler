import sys

a = False
for x in xrange(2520, sys.maxint, 20):
	for y in range(2, 21):
		if x % y != 0:
			break
		if y == 20:
			a = True
	if a:
		print x
		break
