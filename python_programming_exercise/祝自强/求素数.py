import math
n=2
for i in range(5,1000000,2):
    bl=0
    if(i%3==0):
        bl=1
    else:
        for j in range(2,int(math.sqrt(i))+1):
            if(i%j==0):
                bl=1
                break
    if(bl==0):
        n+=1
print (n)