lst = []

for a in xrange(2, 101):
	for b in xrange(2,101):
		if a**b not in lst:
			lst.append(a**b)
print len(lst)