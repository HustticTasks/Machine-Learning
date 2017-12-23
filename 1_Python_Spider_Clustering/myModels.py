import re
import requests
import collections
import bs4
import time

def getHTML(url,proxies):
    try:
        print(url)
        r=requests.get(url,proxies=proxies)
        r.raise_for_status
        return r.text
    except:
        print('error1\n')

def getTag(html,tagList):
    match=re.findall(r'data-original-title=".*"',html)
    if(len(match)!=1):
        for i in range(len(match)-1):
            tagList.append(match[i].split('"')[1])

def getURLlist(listpage,tmpDict,proxies):
    try:
        a=requests.get(listpage,proxies=proxies)
        a.raise_for_status
        soup=bs4.BeautifulSoup(a.text,"html.parser")
        ls=soup.findAll('section',class_="stream-list__item")
        for sec in ls:
            tmp1=re.findall(r'<h2 class="title"><a href="/q/10100000.*"',str(sec))
            tmp2=re.findall(r'<span>.*</span>',str(sec))
            tmp3=str(tmp2[0])[6:-7]
            if(tmp3[-1]=='k'):
                tmp3=float(tmp3[:-1])*1000
            tmpDict['https://segmentfault.com'+tmp1[0].split('"')[3]]=int(tmp3)
    except:
        print('error2\n')

def getFAQ(html,FAQlist):
    soup=bs4.BeautifulSoup(html,"html.parser")
    dr = re.compile(r'<[^>]+>',re.S)
    FAQ=['question:']
    FAQ.append(dr.sub('',str(soup.find(class_="question fmt"))))
    FAQ.append('answer:')
    tmpA=soup.findAll(class_="answer fmt")
    for tag in tmpA:
        FAQ.append(dr.sub('',str(tag)))
    FAQlist.append(FAQ)

def getUserUrl(html,userUrlList):
    soup=bs4.BeautifulSoup(html,"html.parser")
    userUrlList.append('https://segmentfault.com'+re.findall(r'/u/.*"',str(soup.find(class_="question__author")))[0][:-1])
    for txt in soup.findAll(class_="answer__info--author-name"):
        userUrlList.append('https://segmentfault.com'+re.findall(r'/u/.*?"',str(txt))[0][:-1])

def rmRepeat(ls):
    for i in range(len(ls)-1):
        if(ls.count(ls[i])>1):
            del ls[i]