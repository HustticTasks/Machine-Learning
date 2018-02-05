#coding=utf-8

#这是一个给字符串中元音计数的函数
def cou(s):
	c = [0,0,0,0,0]
	for char in list(s):
		if char == 'a':
			c[0] += 1
		if char == 'e':
			c[1] += 1
		if char == 'i':
			c[2] += 1
		if char == 'o':
			c[3] += 1
		if char == 'u':
			c[4] += 1
	print("a = {:d}\ne = {:d}\ni = {:d}\no = {:d}\nu = {:d}".format(c[0],c[1],c[2],c[3],c[4]))
	return None

string = input()
cou(string)
