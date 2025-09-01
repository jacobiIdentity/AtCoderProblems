#!/usr/bin/env python3
from collections import defaultdict
n,m = map(int,input().split())
a_m = [0]+list(map(int,input().split()))+[n+1]
a_m.sort()
gap = []
k = float('inf')
d = defaultdict(int)
for i in range(1,m+2) :
    tmp = a_m[i]-a_m[i-1]-1
    if tmp > 0 :
        gap.append(tmp)
        k = min(k,tmp)
ans = 0
for g in gap :
    ans += g//k + (1 if g%k else 0)
print(ans)

        
