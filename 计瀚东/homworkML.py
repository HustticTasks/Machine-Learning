from math import sqrt
def check(n):
	if n == 1:
        	return False
    	for i in range(2, int(sqrt(n))+1):
        	if n % i == 0:
            		return False
    	return True

cal = 0
num = 1
while(num <= 1000000):
	if(check(num)):
		cal += 1
	num += 1
print cal
	
