from datetime import datetime
start = datetime.now()
x = 28123
adun = []
lst = [1]*x

for a in xrange(2, x):
	q = 0
	for b in xrange(1, a):
		if a % b == 0:
			q += b
	if q > a:
		adun.append(a)

for a in adun:
	for b in adun:
		if a + b < len(lst):
			lst[a+b] = 0

y = 0
for a in xrange(x):
	if lst[a] == 1:
		y += a
print y
print datetime.now() - start