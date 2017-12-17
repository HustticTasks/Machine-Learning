#coding=utf-8
import urllib2
import cookielib
	#设置保存cookie的文件，同级目录下的cookie.txt
filename = 'cookie.txt'
	#声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
ccc = cookielib.CookieJar(filename)
	#利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
handler= urllib2.HTTPCookieProcessor(ccc)
	#通过handler来构建opener
opener = urllib2.build_opener(handler)


	#               保存cookie                  cookie处理器                打开网站的工具
	#                  ccc ----------------------> handle --------------------> opener
	#       CookieJar()    HTTPCookieProcessor(ccc)       build_opener(handler)

	
	#此处的open方法同urllib2的urlopen方法，也可以传入request
	#(urlopen可以理解成opener的一个特殊实例，传入的参数仅仅是url，data，timeout

response=opener.open(https://www.baidu.com/)

	#用如下代码展示
	#	for item in cookie:
	#		print 'Name = '+item.name
	#	print 'Value = '+item.value


	#ignore_discard的意思是即使cookies将被丢弃也将它保存下来
	#ignore_expires的意思是如果在该文件中cookies已经存在，则覆盖原文件写入
ccc.save(ignore_discard=True, ignore_expries=True)

	#CookieJar —-派生—->FileCookieJar  —-派生—–>MozillaCookieJar和LWPCookieJar
