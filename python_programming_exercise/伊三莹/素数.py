from math import sqrt


def primeNumber(n):
    for i in range(2, n):
        count = 0
        flag = 0
        for j in range(2, int(sqrt(i))+1):
            if i % j == 0:
                flag = 1
                break
        if flag == 0:
            count += 1
            print(i)



primeNumber(1000000)




