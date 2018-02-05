#coding=utf-8

#这是一个颠倒字符串的函数
def rev(s):
	a = list(s)
	a.reverse()
	return (''.join(a))

string = input()
print(rev(string))
