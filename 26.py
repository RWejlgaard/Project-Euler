from decimal import *
q = 0
z = 0
y = ''
h = '1'
getcontext().prec = 2000

for a in xrange(1000, 2, -1):
	y = str(1/Decimal(a))[2:]
	for b in xrange(2, 1000):
		if y[0:b] == y[b:b * 2] and y[0:b - 1] != y[b - 1:(b - 1) * 2]:
			if h * (len(y[0:b]) / len(h)) != y[0:b]:
				#print a, ' ', b
				h = y[0:b]
				if b > z:
					z = b
					q = a
print q, ' ', z