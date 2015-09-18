x = 1
y = 1
count = 2

while max(len(str(x)),len(str(y))) != 1000:
	if x > y:
		y = x + y
	else:
		x = x + y
	count += 1
print count