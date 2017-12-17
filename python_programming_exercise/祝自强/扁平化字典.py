def low(dt):
    n=0
    for i in list(dt):
        if(isinstance(dt[str(i)],dict)):
            n+=1
            for j in dt[str(i)]:
                dt[str(i)+'.'+str(j)]=dt[str(i)][str(j)]
            dt.pop(str(i))
    if (n!=0):
        low(dt)
#        n=0
#        for i in dt:
#            if(isinstance(dt[str(i)],dict)):
#                n+=1
#        if(n==0):
#            break

dt={'a': {'b': {'c': 1, 'd': 2,'n':4}, 'x': 2}}
low(dt)
print(dt)
