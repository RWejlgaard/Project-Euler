from datetime import datetime
start = datetime.now()
lst = [2,3,5]
q = 0

for x in xrange(7, 2001, 2):
	for y in lst:
		if x % y == 0:
			q = 1
			break
	if q == 0:
		lst.append(x)
	q = 0
print datetime.now() - start

c = 0
r = 0
ha = 0
hb = 0

for a in xrange(-999,1000):
	for b in xrange(-999,1000):
		for n in xrange(0,1000):
			if n**2 + a * n + b not in lst:
				break
			else:
				c += 1
		if c > r:
			r = c
			ha = a
			hb = b
			print r, ' ', ha, ' ', hb
		c = 0
print r, ' ', ha, ' ', hb
print ha * hb
print datetime.now() - start