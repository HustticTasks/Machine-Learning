print (2)
print (3)
for i in range(4,20):
    bl=0
    for j in range(2,i-1):
        if(i%j==0):
            bl=1
            break
    if(bl==0):
        print(i)