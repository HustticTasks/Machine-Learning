import math
MAX_INT = 1000000
marks_bool = [True] * (MAX_INT + 1)
for i in range(2,int(math.sqrt(MAX_INT)) + 1):
    j = i
    while i * j <= MAX_INT:
        marks_bool[i * j] = False
        j += 1
sum_num = 0
for i in range(2,MAX_INT + 1):
    if marks_bool[i] is True:
        sum_num += 1
print (sum_num)