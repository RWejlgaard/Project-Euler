g = open('22.txt', 'r')
lst = ([line.split('","') for line in g.readlines()])
lst = lst[0]
lst[0] = lst[0][1:5]
lst[5162] = lst[5162][0:6]
lst = sorted(lst)

h = 'abcdefghijklmnopqrstuvwxyz'.upper()
alp = {}

for a in range(len(h)):
	alp[h[a]] = a + 1

x = 0

for a in xrange(len(lst)):
	y = 0
	for b in range(len(lst[a])):
		y += alp[lst[a][b]]
	x += y * (a + 1)
print x