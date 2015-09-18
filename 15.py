import numpy as np

data = np.arange(441) * 0 + 1
data = data.reshape(21, 21)
data = data.astype(long)

for a in range(1, 21):
	for b in range(1, 21):
		data[a, b] = data[a - 1, b] + data[a, b - 1]

print data[20, 20]