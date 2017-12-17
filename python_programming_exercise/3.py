d = {'a': {'b': {'c': 1, 'd': 2}, 'x': 2}}
d1 = {}
def flatmap(d,pre=''):
	for key, value in d.items():
		if isinstance(value, dict):
			flatmap(value,pre = pre + key +'.')
		else:
			d1[pre + key] = value
flatmap(d)
print(d1)
