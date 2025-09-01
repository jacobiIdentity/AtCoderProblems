#!/usr/bin/env python3
from collections import defaultdict
n = int(input())
d_n = list(map(int,input().split())) 
d =defaultdict(int)
for i in range(n) :
    d[d_n[i]] += 1
# print(d)
if 0 not in d or d[0]>1 or d_n[0]>0 :
    print(0)
    exit()
ans = 1
for i in range(1,max(d)+1) :
    if i not in d :
        ans = 0
        break
    ans *= pow(d[i-1],d[i],998244353)
    ans %= 998244353 
print(ans)