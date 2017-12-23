#coding:utf-8
import urllib2
import re

class Segmentfault():
        def __init__(self,baseUrl):
                self.baseURL = baseUrl
        #抓取每一页的帖子
        def messageScratch(self,start,end):
                #对每一页进行抓取
                for pageNum in range(start,end+1):
                        #抓取单页内容
                        url = self.baseURL + r'questions?page=' + str(pageNum)
                        req = urllib2.Request(url)
                        response = urllib2.urlopen(req)
                        #匹配出每条消息的用户名和贴子信息
                        partten = re.compile("href=\"/u/[^\"]+\">[^<]+|data-original-title=\"[^:\\][^\"]+?\"",re.S)
                        results = re.findall(partten,response.read())
			f = open('Result第%d页抓取内容保存.txt' % pageNum,'a')
                        for item in results:
                                f.write(item+' ')
                        #验证访问成功
                        print '已访问'+url
			f.close()
                return None

baseUrl = 'https://segmentfault.com/'
seg = Segmentfault(baseUrl)
print '从哪页开始抓取？到哪页结束？：'
start = int(raw_input())
end = int(raw_input())
seg.messageScratch(start,end)
print '已将抓取结果填入文件'
