#!/usr/bin/env python3
# import scipy.stats
n = int(input())
# print(scipy.stats.hmean(list(map(int,input().split())))/n)
a_n = list(map(int,input().split()))
prd = 1
for i in range(n) :
    prd *= a_n[i]
tmp = 0
for i in range(n) :
    tmp += prd//a_n[i]
print(prd/tmp)