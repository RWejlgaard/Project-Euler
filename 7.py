lst = [2, 3, 5]
i = 7

while len(lst) <= 10000:
	for a in lst:
		if i % a == 0:
			break
		if a == lst[len(lst) - 1]:
			lst.append(i)
	i += 2

print(lst[10000])