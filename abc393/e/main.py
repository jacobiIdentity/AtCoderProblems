#!/usr/bin/env python3
from collections import defaultdict
n,k = map(int,input().split())
a_n = list(map(int,input().split()))
# pList = eratosthenes(max(a_n))
d1 = defaultdict(set)
d2 = defaultdict(set)
d3 = set()
for i in range(n) :
    j = 1
    while j*j <= a_n[i] :
        j2 = a_n[i]//j
        if a_n[i]%j == 0 :
            d1[i].add(j)
            d2[j].add(i)
            if j2 != j :
                d1[i].add(j2)
                d2[j2].add(i)
            if len(d2[j]) == k :
                d3.add(j)
            if len(d2[j2]) == k :
                d3.add(j2)
        j += 1
# d3 = {i for i in d2 if d2[i] >= k}
ans = [1]*n
for j in d3 : 
    for i in d2[j] :
        ans[i] = max(ans[i],j)

print(*ans,sep="\n")
