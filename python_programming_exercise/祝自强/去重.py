ls=[1,2,2,3,4,5]
for i in range(len(ls)-1):
    if(ls.count(ls[i])>1):
        del ls[i]
print(ls)