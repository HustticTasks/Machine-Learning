def no_repeat(l):
    n_l=[l[0]]
    for i in range(1,len(l)):
        t=1
        for j in n_l:
            if j==l[i]:
                t=0
                break
        if t==1:
            n_l.append(l[i])
    print n_l


l=[2,2,1,1,2,2,2,3,3,4,5,5,5,5,77,7,7,6]
no_repeat(l)
