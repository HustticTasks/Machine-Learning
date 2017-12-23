from myModels import *
URLlist=[]
userUrlList=[]
tmpDict={}
baseListPage='https://segmentfault.com/questions?page='
for i in range(1,11):#5686
    listpage=baseListPage+str(i)
    getURLlist(listpage,tmpDict)
    print(listpage)
URLlist=sorted(tmpDict.items(), key=lambda x:x[1], reverse=True)
for url in URLlist:
    html=getHTML(url[0])
    getUserUrl(html,userUrlList)
