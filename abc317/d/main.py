#!/usr/bin/env python3
from collections import defaultdict
n = int(input())
tGiseki, aGiseki = 0, 0
sabun_giseki = []
for _ in range(n) :
    x, y, z = map(int, input().split())
    if x > y :
        tGiseki += z
    else :
        aGiseki += z
        sabun_giseki.append(((y-x+1)//2, z))
minGiseki = (aGiseki- tGiseki+1)//2
# print(sabun_giseki)
# print(aGiseki)
# print(tGiseki)
# print(minGiseki)
if minGiseki < 1 :
    print(0)
    exit()
# sabun_giseki.sort( key=lambda x:(-x[1],x[0]))
dp = [float('inf')]*(minGiseki+1)
dp[0] = 0
for dif,z in (sabun_giseki) :
    for i in reversed(range(z,aGiseki+1)) :
        if 0<=i-z<minGiseki+1 and  dp[i-z] != float('inf') :
            dp[min(i,minGiseki)] = min(dp[min(i,minGiseki)],dp[i-z]+dif)
print(dp[-1])        
# print(dp)