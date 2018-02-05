#coding=utf-8

def check(s):
	a = list(s)
	b = []
	for x in range(0,len(a)):
		b.append(a[len(a)-x-1])
	if a == b:
		return "Yes"
	return "No"

string = input('Please enter a word:')
print(check(string))
