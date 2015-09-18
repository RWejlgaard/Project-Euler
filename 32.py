def reLoop(i):
	p = 0
	for x in range(i,10000):
		p = x * i
		a = str(p) + str(x) + str(i)
		if len(a) == 9:
			a = sorted(a)
			if a == arr and p not in lst:
				lst.append(p)



arr = ["1","2","3","4","5","6","7","8","9"]
lst = []

for i in range(1,100):
	reLoop(i)
print(sum(lst))