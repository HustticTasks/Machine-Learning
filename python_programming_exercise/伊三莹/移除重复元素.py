aList = ['4', '6', '8', '12', '8', '4', 'K', '34', '56', '电脑']
temp = list(set(aList))
temp.sort(key=aList.index)
print(temp)