sunday = 0
day = 1
x = 30 * 4 + 31 * 7
t = 1

for a in xrange(1901, 2001):
	if a % 400 == 0:
		x += 29
	elif a % 4 == 0:
		x += 29
	else:
		x += 28
	for b in range(1, x + 1):
		day += 1
		if b == t:
			if day == 7:
				sunday += 1
			if t == 1: # january
				t += 31
			elif t == 32: # february
				if x % 2 == 0:
					t += 29
				else:
					t += 28
			elif t == 60 or t == 61: # march
				t += 31
			elif t == 91 or t == 92: # april
				t += 30
			elif t == 121 or t == 122: # may
				t += 31
			elif t == 152 or t == 153: # june
				t += 30
			elif t == 182 or t == 183: # july
				t += 31
			elif t == 213 or t == 214: # august
				t += 31
			elif t == 244 or t == 245: # september
				t += 30
			elif t == 274 or t == 275: # october
				t += 31
			elif t == 305 or t == 306: # november
				t += 30
			elif t == 335 or t == 336: # december
				t += 31
		if day == 7:
			day = 0
	t = 1
	if x % 2 == 0:
		x -= 29
	else:
		x -= 28
print sunday