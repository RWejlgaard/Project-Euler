with open('output.txt', 'r') as f:
	lst1 = [line.strip() for line in f]
with open('primes-to-100k.txt', 'r') as f:
	lst2 = [line.strip() for line in f]

b = False
lst3 = []
for x in lst1:
	for y in lst2:
		if x == y:
			b = True
			break
	if not b:
		lst3.append(x)
	b = False

lst4 = []
for x in lst2:
	for y in lst1:
		if x == y:
			b = True
			break
	if not b:
		lst4.append(x)
	b = False

print(lst3)
print(lst4)