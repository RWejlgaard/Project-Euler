import math
import numpy as np

def atkin(limit):
	if limit % 2 != 0:
		limit += 1
	lstSieve = np.zeros((limit), dtype = bool)#[False] * limit
	highest_factor = int(math.floor(math.sqrt(limit))) + 1

	for x in range(1, highest_factor):
		for y in range(1, highest_factor):
			n = 4 * x**2 + y**2
			if n <= limit and n % 60 in (1, 13, 17, 29, 37, 41, 49, 53):
				lstSieve[n] = not lstSieve[n]

			n = 3 * x**2 + y**2
			if n <= limit and n % 60 in (7, 19, 31, 43):
				lstSieve[n] = not lstSieve[n]

			n = 3 * x**2 - y**2
			if n <= limit and x > y and n % 60 in (11, 23, 47, 59):
				lstSieve[n] = not lstSieve[n]
	for x in range(7, highest_factor, 2):
		if lstSieve[x]:
			for y in range(x**2, limit, x**2):
				lstSieve[y] = False
	for x in range(7, limit + 1, 2):
		if lstSieve[x]:
			lstPrimes.append(x)

lstPrimes = [2, 3, 5]

q = 600851475143
g = 5

for x in range(3,600851475143, 2):
	if q % x == 0 and q / x <= 536870912:
		q = int(math.ceil(q / x))
		print(x)
		break
	#if int(math.log10(x)) == g:
	#	print(g)
	#	g += 1

print(q)

atkin(q)

print(len(lstPrimes))

for x in lstPrimes[::-1]:
	if q % x == 0:
		print(x)
		break