import requests
import bs4

def getHTMLText(url):
    if (url==None):
        print('Null\n')
    else:
        try: 
            r=requests.get(url)
            r.raise_for_status
            r.encoding=r.apparent_encoding
            return r.text
        except:
            print('Error!')
            exit()

def fillUnivList(ulist):
    url="http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html"
    soup=bs4.BeautifulSoup(getHTMLText(url),"html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr,bs4.element.Tag):
            tds=tr('td')
            ulist.append([tds[0].string,tds[1].string,tds[2].string])

def printUnivList(ulist,num):
    print("{:^10}\t{:^6}\t{:^10}".format("排名","学校","省份"))
    for i in range(num):
        u=ulist[i]
        print("{:^10}\t{:^6}\t{:^10}".format(u[0],u[1],u[2]))

uinfo=[]
fillUnivList(uinfo)
printUnivList(uinfo,10)


