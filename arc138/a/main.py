#!/usr/bin/env python3
from collections import defaultdict
n,k = map(int,input().split())
a_n = list(map(int,input().split()))
firstK = a_n[:k]
firstK.sort()
d = defaultdict(int)
for i in range(k) :
    d[a_n[i]] = max(d[a_n[i]],i)
i,j = 0,k
ans = float('inf')
while i< k and j<n :
    if firstK[i] < a_n[j] :
        while i<k and firstK[i] < a_n[j] :
            # ans = min(ans,k-1- d[firstK[i]]+j-k+1)
            ans = min(ans,j- d[firstK[i]])
            i += 1
    j += 1
if ans == float('inf') :
    ans = -1
print(ans)