list = ['a','b','b','cc','a','cc','de','ac','de','ac']
#['a','b','cc','de','ac']
i = 0
while(i < len(list)):
	k = i + 1
	while(k < len(list)):
		if(list[i] == list[k]):
			list.pop(k)
		else:
			k += 1
	i += 1
print(list)