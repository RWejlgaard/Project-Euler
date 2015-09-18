import sys
lst = [2, 3, 5]
x = 10

for i in xrange(7, 2000000, 2):
	for a in lst[:]:
		if i % a == 0:
			break
		if a == lst[len(lst) - 1]:
			lst.append(i)
			x += i
print x