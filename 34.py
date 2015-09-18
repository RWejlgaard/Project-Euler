import math

def reLoop():
	global depth, count, asum
	depth += 1
	for x in range(1,10):
		lst[depth] = x

		if depth > 0:
			a = 0
			b = ""
			for x in range(0, depth):
				if lst[x] != 0:
					a += math.factorial(lst[x])
					b += str(lst[x])
			if str(a) == b:
				asum += a
				print(asum)

		if depth < count:
			reLoop()
	depth -= 1

count = 8
depth = -1
asum = 0
lst = []
for x in range(1,10):
	lst.append(0)
reLoop()
print(asum)