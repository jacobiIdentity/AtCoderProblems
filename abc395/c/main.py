#!/usr/bin/env python3
from collections import defaultdict
n = int(input())
a_n= list(map(int,input().split()))
d = defaultdict(list)
ans = float('inf')
for i in range(n) :
    if a_n[i] in d :
        ans = min(ans,i-d[a_n[i]][-1]+1)
    d[a_n[i]].append(i)
if ans == float('inf') : ans = -1
print(ans)