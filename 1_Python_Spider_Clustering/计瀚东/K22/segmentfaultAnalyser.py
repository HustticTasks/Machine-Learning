#coding=utf-8
import urllib2
import urllib
import re
import operator
import numpy as np

class Analyser():
	def __init__(self):
		pass
	def messageAnalysis(self,userJar,labelJar,pages):
		#对匹配出的信息进行修剪，同时归类到userJar和labelJar中
		for pageNum in range(1,pages+1):
			f = open('Result第%d页抓取内容保存.txt' % pageNum,'r')
			results = f.read().split()
                	for i in range(0,len(results)):
                		test = results[i].split('\"')[0]
                        	if test == 'href=':
                                	userName = results[i].split('>')[1]
                                	if userName not in userJar:
                                		userJar.append(userName)
                        	else:
                                	labelName = results[i].split('\"')[1]
                                	if labelName not in labelJar:
                                		labelJar.append(labelName)
                	f.close()
			print '第%d页信息的用户名和标签名已导入' % pageNum
		return None

	#统计数据写入矩阵
	def calculate(self,dataJar,users,labels,pages):
		userNum = len(users)
		labelNum = len(labels)
		for pageNum in range(1,pages+1):
                        f = open('Result第%d页抓取内容保存.txt' % pageNum,'r')
                        results = f.read().split()
			#依次填入数据
			i = 0
			for n in range(0,len(results)):
				#检查是否为用户名
                        	test = results[n].split('\"')[0]
                        	if test == 'href=':
					userName = results[n].split('>')[1]
					for number in range(0,userNum):
						if userName == users[number]:
							i = number
							break
				else:
					j = 0
					labelName = results[n].split('\"')[1]
					for number in range(0,labelNum):
						if labelName == labels[number]:
							j = number
							break
					dataJar[i,j] += 1
			f.close()
			print '第%d页贴子含有的标签数已经计入矩阵' % pageNum	
		return None
	#统计一下各标签的热度
	def hotLabels(self,dataSet,labels,labelNum,pages):
		hotLabelJar = {}
		labelDataSet = np.sum(dataSet.copy(),0)
		for i in range(0,labelNum):
			hotLabelJar.setdefault(labels[i],labelDataSet[i])
		sortedHotLabelJar = sorted(hotLabelJar.iteritems(),key=operator.itemgetter(1),reverse=True)
		#写入文件
		f = open('YLabel标签在%d页中的热度.txt' % pages,'a')
		f.write('各标签名字及其热度：'+'\n')
		for labelAhot in sortedHotLabelJar:
			f.write(labelAhot[0]+'              ')
			f.write(str(labelAhot[1])+'\n')
		f.close()
		print '已完成将各标签及其热度以降序排列写入文件'
		return 0

#聚类分析用的递归函数
def reClassify(datas,Klists,userNum,K):
        #按照上次的聚类结果再找出中点
        middlePointJar = []
        for eachList in Klists:
                eachClassUsers = datas[eachList,]
                eachClassMiddlePoint = np.sum(eachClassUsers,0)/2
                eachClassMiddlePoint = np.tile(eachClassMiddlePoint,(1,1))
                middlePointJar.append(eachClassMiddlePoint)
        newKcenters = np.concatenate(middlePointJar,0)
        newKlists = []
	for i in range(0,K):
		newKlists.append([])
	for i in range(0,userNum):
        	differences = np.tile(datas[i,].copy(),(K,1)) - newKcenters
        	squareDifferences = differences**2
        	addSquare = np.sum(squareDifferences,1)
        	classify = 0
        	for j in range(1,len(Klists)):
                	if addSquare[j] < addSquare[classify]:
                        	classify = j
        	newKlists[classify].append(i)
        return newKlists

print '对已抓取的多少页结果进行分析（请确保您要分析的内容已将被抓取）：'
users = []
labels = []
pages = int(raw_input())
seg = Analyser()
seg.messageAnalysis(users,labels,pages)
userNum = len(users)
labelNum = len(labels)
#展示抓取结果
datas = np.zeros((userNum,labelNum))
seg.calculate(datas,users,labels,pages)
print '发现%d名用户' % userNum
print '发现%d个标签' % labelNum

#去除发帖量少于某值的用户，减少运算量
#创建两个列表分别用来储存所有不符合要求的用户编号和用户名
deleteNumberList = []
deleteUserList = []
print '将忽略总标签数小于多少的用户？'
limit = int(raw_input())
for eachUser in range(0,userNum):
	if eachUser == np.shape(datas)[0]:
		break
	messageNum = 0
	for eachLabel in range(0,labelNum):
		messageNum += datas[eachUser,eachLabel]
	if messageNum < limit:
		deleteNumberList.append(eachUser)
		print '第%d名用户不符合要求' % eachUser
	else:
		print '第%d用户符合要求' % eachUser
for number in deleteNumberList:
	deleteUserList.append(users[number])
#开始对照清单在用户清单和数据集批量删除用户
for name in deleteUserList:
	users.remove(name)
	print '已将用户%s移除'%name
datas = np.delete(datas,deleteNumberList,0)
#重新计算用户数量并展示
userNum = len(users)
print '去除总发贴数小于%d的用户后剩余%d名用户' % (limit,userNum)

#附加统计各标签的热度
seg.hotLabels(datas,labels,labelNum,pages)
print '将设置几个类来进行聚类分析？'
K = int(raw_input())
#开始使用K-means算法进行数据分析
Kcenters = datas[0:K,].copy()
Klists = []
for i in range(0,K):
	Klists.append([])
for i in range(0,userNum):
	differences = np.tile(datas[i,].copy(),(K,1)) - Kcenters
	squareDifferences = differences**2
	addSquare = np.sum(squareDifferences,1)
	classify = 0
	for j in range(1,K):
		if addSquare[j] < addSquare[classify]:
			classify = j
	Klists[classify].append(i)
#此处使用一个循环来递归判断
while True:
	newKlists = reClassify(datas,Klists,userNum,K)
	for i in range(0,len(newKlists)):
		if Klists[i] != newKlists[i]:
			Klists = newKlists
			continue
	break
#将分类好的信息写入文件便于人工判断聚类结果
for i in range(0,len(Klists)):
	if len(Klists[i]) == 0:
		continue
	f = open('ZPage%d_K%d_Class%d_Limit%d_Users%d.txt' % (pages,K,i+1,limit,len(Klists[i])),'a')
	f.write('%d页内容中K=%d时限制标签数不小于%d时第%d聚类的用户信息：' % (pages,limit,K,i+1)+'\n')
	for j in range(0,len(Klists[i])):
		f.write('第%d名用户：' % (j+1)+users[Klists[i][j]]+'\n')
		favLabels = {}
		for m in range(0,labelNum):
			if datas[j,m] != 0:
				favLabels.setdefault(labels[m],datas[j,m])
		sortedFavLabels = sorted(favLabels.iteritems(),key=operator.itemgetter(1),reverse=True)
		for labelAfrequency in sortedFavLabels:
			f.write(labelAfrequency[0]+':'+str(labelAfrequency[1])+' ')
		f.write('\n\n')
	f.close()
	print '已完成K=%d时第%d聚类写入文件(含有%d名用户)' % (K,i+1,len(Klists[i]))
print '分析结束'
