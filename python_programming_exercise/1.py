def isprime(i):
	for k in range(2,int(i**0.5) + 1):
		if (i % k)== 0:
			return 0
	return 1
s = 0
for i in range(2,1000001):
	if isprime(i):
		s += 1
print(s)


