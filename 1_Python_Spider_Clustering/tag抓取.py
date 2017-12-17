import re
import requests
def getHTML(url):
    try:
        print(url)
        r=requests.get(url)
        r.raise_for_status
        return r.text
    except:
        print('error1\n')

def getTag(html,tagList):
    match=re.findall(r'data-original-title=".*"',html)
    if(len(match)!=1):
        for i in range(len(match)-1):
            tagList.append(match[i].split('"')[1])

def getURLlist(listpage,URLlist):
    try:
        a=requests.get(listpage)
        a.raise_for_status
        tmp=re.findall(r'<h2 class="title"><a href="/q/10100000.*"',a.text)
        for tag in tmp:
            URLlist.append('https://segmentfault.com'+tag.split('"')[3])
    except:
        print('error2\n')

tagList=[]
URLlist=[]
baseListPage='https://segmentfault.com/questions?page='
for i in range(1,5686):#5686
    listpage=baseListPage+str(i)
    getURLlist(listpage,URLlist)
    print(listpage)
for url in URLlist:
    getTag(getHTML(url),tagList)
fl=open('data.txt','w')  
fl.write(str(tagList));  
fl.close()  
