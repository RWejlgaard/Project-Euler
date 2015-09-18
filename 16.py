from datetime import datetime
start = datetime.now()
g = 2**1000

lst = []
lst = map(int, list(str(g)))

print sum(lst)
print datetime.now() - start