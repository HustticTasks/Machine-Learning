#coding=utf-8



#Skyler.W
#2017.12
import sys
defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)
import requests
import os
from bs4 import BeautifulSoup
import random




class mzitu(object):

    #定义了一个自己的访问网站的方法， 后续还可以考虑加入代理池、更换IP、倒计时等功能
    def hit(self, url):
        headers = {'User-Agent': "Mozilla/5.0 (iPad; CPU OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1",'Referer':'http://m.mzitu.com/101213'}
        content = requests.get(url, headers=headers)
        return content

    #从集成的页面得到图组（set）的网址
    def all_url(self, url):
        html = self.hit(url)
        all_a = BeautifulSoup(html.text, 'lxml').find('div', class_='all').find_all('a')
        print all_a
        for a in all_a:
            title = a.get_text()
            print '                开始保存了呢~：' + title
            path = str(title).replace('?', '_')
            if not self.mkdir(path):#如果文件夹存在则跳过
                print '~~~~~~~~~~~~~~~~文件夹已经存在啦！跳过:%s!'  % title
                continue
            href = a['href']
            self.img_set(href)

    #在图组网址里面获取共有多少张图，以及具体一张图的网址是什么
    def img_set(self, href):
        html = self.hit(href)
        max_span = BeautifulSoup(html.text, 'lxml').find('div', class_='pagenavi').find_all('span')[-2].get_text()
        for span in range(1, int(max_span)+1):
            page_url = href + '/' + str(span)
            self.img_save(page_url)


    #保存图片的方法
    def img_save(self, page_url):
        img_response = self.hit(page_url)
        img_url = BeautifulSoup(img_response.text, 'lxml').find('div', class_ = 'main-image').find('img')['src']
        name = img_url.replace('/', '_')
        try:
            img = self.hit(img_url)
            f = open(name + '.jpg', 'ab')
            f.write(img.content)
            f.close()
            print ">>>>>>>>>>>>>>>>写入成功~" 
        except:
            print '不能写入图片数据：' + img_url
            return False


    

    #创建文件夹，一套图拥有一个自己的文件夹
    def mkdir(self, path):
        path = path.strip()
        is_exists = os.path.exists(os.path.join("/Users/skyler/Documents/mzitu", path))
        if not is_exists:
            print "++++++++++++++++建了一个名字叫'%s'的文件夹。"  % path
            os.makedirs(os.path.join('/Users/skyler/Documents/mzitu',path))
            os.chdir(os.path.join('/Users/skyler/Documents/mzitu',path))
            return True
        else:
            print "~~~~~~~~~~~~~~~~这个文件夹已经存在惹咕叽"
            os.chdir(os.path.join('/Users/skyler/Documents/mzitu',path))
            return False



Mzitu = mzitu()
Mzitu.all_url('http://www.mzitu.com/all')