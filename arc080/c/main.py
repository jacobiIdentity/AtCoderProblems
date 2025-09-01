#!/usr/bin/env python3
from collections import defaultdict
n = int(input())
a_n = list(map(int,input().split()))
d = defaultdict(int)
for i in range(n) :
    d[a_n[i]%4] += 1
isOK = True
if d[2]==1 and d[0]==0 :
    isOK = False
elif d[2]>=2 and d[0]==0 and d[1]+d[3]>=1 :
    isOK = False
elif d[2]>=1 and d[0]<d[1]+d[3] :
    isOK = False
elif d[2]==0 and d[0]+1<d[1]+d[3] :
    isOK = False
print('YNeos'[not(isOK)::2])

