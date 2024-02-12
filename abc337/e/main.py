#!/usr/bin/env python3
import math
n = int(input())
m = math.ceil(math.log2(n))
print(m)
drinks = [[] for _ in range(m)]
for i in range(n) :
    bDigits = format(i, '0'+str(m)+'b')
    # print(bDigits)
    for j in range(m):
        if bDigits[j] == '1' :
            drinks[j].append(i+1)
for j in range(m) :
    print(len(drinks[j]), *drinks[j])
print(int(input(),base=2)+1)