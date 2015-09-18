import time
start = time.clock()
x = 13195
lst = [2, 3, 5]
for i in xrange(2, (x/2+1)):
	if (i % 2 != 0):
		if (i % 3 != 0):
			if (i % 5 != 0):
				lst.append(i)
print len(lst)
for a in lst[:]:
	for b in lst[:]:
		if (b % a == 0 and a != b):
			lst.remove(b)
for c in lst:
	if (x % c == 0):
		print c
print (time.clock() - start)
