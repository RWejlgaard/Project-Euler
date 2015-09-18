from decimal import *
import time

def isPrime(x):
	global r
	if x % 2 != 0 and x % 3 != 0 and x % 5 != 0 and x % 7 != 0:
		lstPascal = [1]
		t = True
		for i in range(0, 70):
			lstPascal.append(int(lstPascal[i] * Decimal((x - i)) / (i + 1)))
			if lstPascal[i + 1] % x != 0:
				t = False
				break
		if t:
			writeResult(x)
			if x > r:
				r = x
			return

def writeResult(x):
	with open("3-3-output.txt", "a") as myfile:
		myfile.write(str(x) + "\n")

start = time.time()

getcontext().prec = 1000
n = 600851475143
h = 0
r = 0

for x in range(2, n):
	#if x % 1000 == 0:
	#	print(x)
	if n % x == 0:
		if x**2 == n or h == x:
			print(r)
			quit()
		else:
			h = x
			isPrime(n / x)
			isPrime(x)
print(time.time() - start)