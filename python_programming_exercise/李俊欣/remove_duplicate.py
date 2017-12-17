m=['a','b','a','c','b']
n=list(set(m))#删除重复元素
n.sort(key=m.index)#索引m原来的的序列，对n进行排序
print(n)
