x = 0
y = 0

for a in range(1, 101):
	x += a**2

for a in range(1, 101):
	y += a
y = y**2
print x
print y
print y - x
