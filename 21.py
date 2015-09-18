lst = []
x = 0

for a in xrange(0, 10000):
	lst.append(0)
	for b in xrange(1, a):
		if a % b == 0:
			lst[a] += b
for a in xrange(0, 10000):
	for b in xrange(0, 10000):
		if a != b and a == lst[b] and b == lst[a]:
			print a, lst[a], b, lst[b]
			x += a
print x