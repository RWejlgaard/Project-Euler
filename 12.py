import sys
from datetime import datetime
start = datetime.now()
i = 1
a = 0
for x in xrange(2, sys.maxint):
	i += x
	if i % 2 == 0:
		for y in xrange(1, i + 1):
			if i % y == 0:
				a += 1
		if a > 500:
			break
		a = 0
print i
print a
print datetime.now() - start