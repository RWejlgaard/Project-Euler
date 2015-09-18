import time
start = time.clock()

def cal():
	for i in xrange(f, t):
		if (i %2 != 0):
			if (i % 3 != 0):
				if (i % 5 != 0):
					lst.append(i)
	#print lst
	for a in lst[:]:
		for b in lst[:]:
			if (b % a == 0 and a != b):
				#print b
				lst.remove(b)
	#print lst
	for c in lst[:]:
		if (x % c != 0):
			lst.remove(c)

x = 600851475143
lst = [2, 3, 5]
f = 2
t = 20000
count = 0
while t < x/2:
	cal()
	f = t + 1
	t = t + 20000
	print lst
	print (time.clock() - start)
	count += 1
	print count
f = t - 20000 + 1
t = x/2
cal()
print lst
print (time.clock() - start)