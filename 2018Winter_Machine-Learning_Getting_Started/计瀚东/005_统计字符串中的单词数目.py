#coding=utf-8

#这是一个统计字符串中单词数目的函数
def count(s):
	a = s.split()
	return len(a)

string = input("Please enter some words:")
print("There are {:2d} words.".format(count(string)))
