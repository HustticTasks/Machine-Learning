#coding=utf-8

def latig(s):
	a = list(s)
	for char in a:
		if (char != 'a') and (char != 'e') and (char != 'i') and (char !='o') and (char != 'u'):
			a.remove(char)
			b = ['-', char, 'a', 'y']
			a.extend(b)
			break
	return (''.join(a))

string = input("Please input a word:")
print(latig(string))
