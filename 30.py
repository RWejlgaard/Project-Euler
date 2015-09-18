import sys
import numpy as np

x = 0

for a in xrange(2, 500000):
	data = np.array(0)
	for b in str(a):
		data = np.append(data, int(b))
	if a == sum(data**5):
		print a
		x += a
print x