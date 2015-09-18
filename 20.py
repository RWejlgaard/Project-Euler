import math
x = str(math.factorial(100))
y = 0
for a in xrange(len(x)):
	y += int(x[a])
print y