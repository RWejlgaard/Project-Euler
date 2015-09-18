from decimal import *
getcontext().prec = 1000

x = 6857

if x % 2 != 0 and x % 3 != 0 and x % 5 != 0 and x % 7 != 0:
	lstPascal = [1]
	t = True
	for i in range(0, 9):
		lstPascal.append(int(lstPascal[i] * Decimal((x - i)) / (i + 1)))
		if lstPascal[i + 1] % x != 0:
			print(lstPascal)
			print(i)
			t = False
			break
	if t:
		print(x)
		if x > r:
			r = x
		quit()