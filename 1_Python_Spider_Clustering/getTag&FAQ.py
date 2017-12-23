from myModels import *
URLlist=[]
tagList=[]
FAQlist=[]
tmpDict={}
proxies={  
        "http":"http://219.138.58.99:3128",
        "http":"http://119.122.30.113:9000", 
        "http":"http://221.217.49.196:9000", 
        "http":"http://116.226.112.113:9000",
        "http":"http://125.93.193.137:3128",
        "http":"http://58.244.52.31:8080",
        "http":"http://113.118.97.119:9797",
        "http":"http://122.114.122.212:9999",
        "http":"http://122.72.18.60:80"
        }
baseListPage='https://segmentfault.com/questions?page='
for i in range(1,5686):#5686
    listpage=baseListPage+str(i)
    getURLlist(listpage,tmpDict,proxies)
    time.sleep(0.5)
    print(listpage)
URLlist=sorted(tmpDict.items(), key=lambda x:x[1], reverse=True)
with open('url.txt','w',encoding='utf-8') as f2:
    for item in URLlist:
        f2.write(item[0]+'\n')
    f2.close()
for url in URLlist:
    html=getHTML(url[0],proxies)
    getTag(html,tagList)
    time.sleep(0.5)
    #getFAQ(html,FAQlist)
#with open('FAQ.txt','w',encoding='utf-8') as f1:
    #f1.write(str(FAQlist))
    #f1.close()
with open('tag.txt','w',encoding='utf-8') as f3:
    for tag in tagList:
        f3.write(tag+',')
    f3.close()
