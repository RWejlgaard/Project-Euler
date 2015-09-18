import time

def c(z):
	for x in range(1,z):
		pass

for x in range(1,8):
	start = time.time()
	c(100 * 10**x)
	print(time.time() - start)