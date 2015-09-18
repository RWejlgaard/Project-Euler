from datetime import datetime
start = datetime.now()
x = 9
y = 0
g = ''
count = 0

def recurse():
	global x
	global y
	global g
	global count
	if x > y:
		for a in xrange(0, x + 1):
			if str(a) not in g:
				g += str(a)
				y += 1
				recurse()
				g = g[:-1]
	else:
		for a in xrange(0, x + 1):
			if str(a) not in g:
				count += 1
				if count == 1000000:
					print g + str(a)
					print datetime.now() - start
					quit()
	y -= 1
recurse()